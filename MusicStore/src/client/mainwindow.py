from tkinter import *
import tkinter.messagebox as mesbox
import requests
from  my_app import create_app

font = ('Arial Bold', 16)

root = Tk()
root.title("My GUI")  
root.geometry('800x600')

username = StringVar()
userpassword = StringVar()

def check_login(username: str, password: str):
    data = f'{{ "username": "{username}", "password": "{password}" }}'
    r = requests.post('http://127.0.0.1:8000/login/log', data=data)
    answer = r.json()
    print(answer)
    code = answer["code"]
    message = answer["message"]
    if code != 200:
        print(f"Server error:{message}")
        return None
    else:
        return answer["id"][0]


def open_login():
    post = check_login(username=username.get(),password=userpassword.get())
    if post:
        print("Login ok")
        print(post)
        root.withdraw()
        create_app(root,font)
    else:
        mesbox.showerror(title="Wrong login",message="Логин или пароль не верны")




lbl_main = Label(root, text="Вход в систему", font=font)
lbl_login = Label(root, text="Логин", font=font)
lbl_pass = Label(root, text='Пароль', font=font)

entry_login = Entry(root, font=font, textvariable=username)
entry_pass = Entry(root, font=font,show="*", textvariable=userpassword)

btn_enter = Button(root, text='Вход', font=font, command=open_login)
btn_close = Button(root, text='Отмена', font=font)

lbl_main.grid(row=0, columnspan=2, column=1)
lbl_login.grid(row=1, column=0, pady=10, ipadx=10)
lbl_pass.grid(row=2, column=0, pady=10, ipadx=10)

entry_login.grid(row=1, column=1, columnspan=3, padx=30, pady=10)
entry_pass.grid(row=2, column=1, columnspan=3, padx=30, pady=10)

btn_enter.grid(row=3, column=1, pady=10)
btn_close.grid(row=3, column=2, pady=10)

if __name__ == '__main__':
    root.mainloop()