import requests
from tkinter import *

def create_manager_app(root,font):
    manager_app = Toplevel(root)
    manager_app.title("Работа с manager")  
    manager_app.geometry('800x600')

    
    get_id = StringVar()
    upd_id = StringVar()
    del_id = StringVar()

    upd_user_id = StringVar()
    new_user_id = StringVar()

    

    lbl_get_manager = Label(manager_app, text="Показать manager по id", font=font)
    entry_get_manager = Entry(manager_app, font=font, textvariable=get_id)
    btn_get_manager = Button(manager_app, text='Получить', font=font, command=lambda: fun_get_manager(entry_get_manager.get()))
    lbl_get_manager.grid(row=1, column=1)
    entry_get_manager.grid(row=2, column=0)
    btn_get_manager.grid(row=2, column=2)


    lbl_new_manager = Label(manager_app, text='Добавить нового manager', font=font)
    lbl_new_user_id = Label(manager_app, text='Введите user_id для нового manager', font=font)
    entry_user_id_data = Entry(manager_app, font=font, textvariable=new_user_id)
    btn_new_user_id = Button(manager_app, text='Создать', font=font, command=lambda: fun_new_manager(entry_user_id_data.get()))

    lbl_new_manager.grid(row=3, column=1)
    lbl_new_user_id.grid(row=4, column=0)
    entry_user_id_data.grid(row=4, column=2)
    btn_new_user_id.grid(row=5, column=1)


    lbl_upd_manager = Label(manager_app, text='Обновить manager по id', font=font)
    lbl_upd_manager_id = Label(manager_app, text='Введите id', font=font)
    entry_upd_manager = Entry(manager_app, font=font, textvariable=upd_id)
    lbl_upd_manager_username = Label(manager_app, text='Введите новый user_id для работы manager', font=font)
    entry_upd_user_id = Entry(manager_app, font=font, textvariable=upd_user_id)
    btn_upd_manager = Button(manager_app, text='Обновить', font=font, command=lambda: fun_upd_manager(entry_upd_manager.get(),entry_upd_user_id.get()))

    lbl_upd_manager.grid(row=6, column=1)
    lbl_upd_manager_id.grid(row=7, column=0)
    entry_upd_manager.grid(row=7, column=2)
    lbl_upd_manager_username.grid(row=8, column=0)
    entry_upd_user_id.grid(row=8, column=2)
    btn_upd_manager.grid(row=9, column=1)


    lbl_del_manager = Label(manager_app, text='Удалить manager по id', font=font)
    entry_del_manager = Entry(manager_app, font=font, textvariable=del_id)
    btn_del_manager = Button(manager_app, text='Удалить', font=font, command=lambda: fun_del_manager(entry_del_manager.get()))

    lbl_del_manager.grid(row=10, column=1)
    entry_del_manager.grid(row=11, column=0)
    btn_del_manager.grid(row=11, column=2)



def fun_get_manager(manager_id):
   r = requests.get(f'http://127.0.0.1:8000/manager/{manager_id}')
   answer = r.json()
   print(answer)

def fun_new_manager(user_id):
   data = f'{{ "user_id": "{user_id}"}}'
   r = requests.post(f'http://127.0.0.1:8000/manager/',data=data)
   answer = r.json()
   print(answer)

def fun_upd_manager(manager_id,user_id):
   data = f'{{ "user_id": "{user_id}"}}'
   r = requests.put(f'http://127.0.0.1:8000/manager/{manager_id}',data=data)
   answer = r.json()
   print(answer)

def fun_del_manager(manager_id):
   r = requests.delete(f'http://127.0.0.1:8000/manager/{manager_id}')
   answer = r.json()
   print(answer)