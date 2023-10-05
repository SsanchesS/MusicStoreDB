import requests
from tkinter import *

def create_user_app(root,font):
    user_app = Toplevel(root)
    user_app.title("Работа с user")  
    user_app.geometry('800x600')

    
    get_id = StringVar()
    upd_id = StringVar()
    del_id = StringVar()

    new_username = StringVar()
    upd_username = StringVar()
    new_userpass = StringVar()
    upd_userpass = StringVar()
    new_usercard = StringVar()
    upd_usercard = StringVar()

    

    lbl_get_user = Label(user_app, text="Показать user по id", font=font)
    entry_get_user = Entry(user_app, font=font, textvariable=get_id)
    btn_get_user = Button(user_app, text='Получить', font=font, command=lambda: fun_get_user(entry_get_user.get()))
    lbl_get_user.grid(row=1, column=1)
    entry_get_user.grid(row=2, column=0)
    btn_get_user.grid(row=2, column=1)


    lbl_new_user = Label(user_app, text='Добавить нового user', font=font)
    lbl_new_user_username = Label(user_app, text='Введите username нового user', font=font)
    entry_new_user_username_data = Entry(user_app, font=font, textvariable=new_username)
    lbl_new_user_password = Label(user_app, text='Введите password нового user', font=font)
    entry_new_user_password_data = Entry(user_app, font=font, textvariable=new_userpass)
    lbl_new_user_card = Label(user_app, text='Введите card нового user', font=font)
    entry_new_user_card_data = Entry(user_app, font=font, textvariable=new_usercard)
    btn_new_user = Button(user_app, text='Создать', font=font, command=lambda: fun_new_user(entry_new_user_username_data.get(),entry_new_user_password_data.get(),entry_new_user_card_data.get()))
    lbl_new_user.grid(row=3, column=1)
    lbl_new_user_username.grid(row=4, column=0)
    entry_new_user_username_data.grid(row=4, column=2)
    lbl_new_user_password.grid(row=5, column=0)
    entry_new_user_password_data.grid(row=5, column=2)
    lbl_new_user_card.grid(row=6, column=0)
    entry_new_user_card_data.grid(row=6, column=2)
    btn_new_user.grid(row=7, column=1)


    lbl_upd_user = Label(user_app, text='Обновить user по id', font=font)
    lbl_upd_user_id = Label(user_app, text='Введите id', font=font)
    entry_upd_user = Entry(user_app, font=font, textvariable=upd_id)
    lbl_upd_user_username = Label(user_app, text='Введите username user', font=font)
    entry_upd_user_username_data = Entry(user_app, font=font, textvariable=upd_username)
    lbl_upd_user_password = Label(user_app, text='Введите password user', font=font)
    entry_upd_user_password_data = Entry(user_app, font=font, textvariable=upd_userpass)
    lbl_upd_user_card = Label(user_app, text='Введите card user', font=font)
    entry_upd_user_card_data = Entry(user_app, font=font, textvariable=upd_usercard)
    btn_upd_user = Button(user_app, text='Обновить', font=font, command=lambda: fun_upd_user(entry_upd_user.get(),entry_upd_user_username_data.get(),entry_upd_user_password_data.get(),entry_upd_user_card_data.get()))
    lbl_upd_user.grid(row=8, column=1)
    lbl_upd_user_id.grid(row=9, column=0)
    entry_upd_user.grid(row=9, column=2)
    lbl_upd_user_username.grid(row=10, column=0)
    entry_upd_user_username_data.grid(row=10, column=2)
    lbl_upd_user_password.grid(row=11, column=0)
    entry_upd_user_password_data.grid(row=11, column=2)
    lbl_upd_user_card.grid(row=12, column=0)
    entry_upd_user_card_data.grid(row=12, column=2)
    btn_upd_user.grid(row=13, column=1)


    lbl_del_user = Label(user_app, text='Удалить user по id', font=font)
    entry_del_user = Entry(user_app, font=font, textvariable=del_id)
    btn_del_user = Button(user_app, text='Удалить', font=font, command=lambda: fun_del_user(entry_del_user.get()))

    lbl_del_user.grid(row=14, column=1)
    entry_del_user.grid(row=15, column=0)
    btn_del_user.grid(row=15, column=1)


def fun_get_user(user_id):
   r = requests.get(f'http://127.0.0.1:8000/users/{user_id}')
   answer = r.json()
   print(answer)

def fun_new_user(username,password,card):
   data = f'{{ "username": "{username}", "password": "{password}", "card": "{card}" }}'
   r = requests.post(f'http://127.0.0.1:8000/users/',data=data)
   answer = r.json()
   print(answer)

def fun_upd_user(user_id,username,password,card):
   data = f'{{ "username": "{username}", "password": "{password}", "card": "{card}" }}'
   r = requests.put(f'http://127.0.0.1:8000/users/{user_id}',data=data)
   answer = r.json()
   print(answer)

def fun_del_user(user_id):
   r = requests.delete(f'http://127.0.0.1:8000/users/{user_id}')
   answer = r.json()
   print(answer)