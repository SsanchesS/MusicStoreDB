from tkinter import *
import tkinter.messagebox as mesbox
import requests
from  my_app import create_app

font = ('Arial Bold', 16)

root = Tk()
root.title("My GUI")  
root.geometry('700x400')

email = StringVar()
phone_number = StringVar()

def check_login(email: str, phone_number: str):
    data = {"email": email, "phone_number": phone_number}
    r = requests.post('http://127.0.0.1:8000/login', json=data) # r = requests.post('http://127.0.0.1:8000/login', data=data)
    answer = r.json()
    print(answer)
    code = answer["code"]
    message = answer["message"]
    if code != 200:
        print(f"Server error:{message}")
        return None
    else:
        return answer["customer_id"][0]

def open_login():
    customer_id = check_login(email=email.get(),phone_number=phone_number.get())
    if customer_id:
        print("Login ok")
        print(f'customer_id: {customer_id}')
        root.withdraw()
        create_app(root,font,customer_id_props=customer_id)
    else:
        mesbox.showerror(title="Wrong login",message="Логин или пароль не верны")

lbl_main = Label(root, text="Вход в систему", font=font)
lbl_email = Label(root, text="email", font=font)
lbl_phone_number = Label(root, text='phone_number', font=font)

entry_email = Entry(root, font=font, textvariable=email)
entry_phone_number = Entry(root, font=font,show="*", textvariable=phone_number)

btn_enter = Button(root, text='Вход', font=font, command=open_login)
btn_close = Button(root, text='Отмена', font=font)

lbl_main.grid(row=0, columnspan=2, column=1)
lbl_email.grid(row=1, column=0, pady=10, ipadx=10)
lbl_phone_number.grid(row=2, column=0, pady=10, ipadx=10)

entry_email.grid(row=1, column=1, columnspan=3, padx=30, pady=10)
entry_phone_number.grid(row=2, column=1, columnspan=3, padx=30, pady=10)

btn_enter.grid(row=3, column=1, pady=10)
btn_close.grid(row=3, column=2, pady=10)

if __name__ == '__main__':
    root.mainloop()