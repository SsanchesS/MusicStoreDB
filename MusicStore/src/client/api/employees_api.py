import requests
from tkinter import *

def create_employees_app(root,font):
   customer_app = Toplevel(root)
   customer_app.title("Работа с Customers")  
   customer_app.geometry('800x600')


   get_id = StringVar()
   upd_id = StringVar()
   del_id = StringVar()

   new_customer_first_name = StringVar()
   upd_customer_first_name = StringVar()

   new_customer_last_name = StringVar()
   upd_customer_last_name = StringVar()

   new_customer_email = StringVar()
   upd_customer_email = StringVar()

   new_customer_phone_number = StringVar()
   upd_customer_phone_number = StringVar()

#

   lbl_get_customer = Label(customer_app, text="Показать customer по id", font=font)
   entry_get_customer = Entry(customer_app, font=font, textvariable=get_id)
   btn_get_customer = Button(customer_app, text='Получить', font=font, command=lambda: fun_get_customer(entry_get_customer.get()))
   lbl_get_customer.grid(row=1, column=1)
   entry_get_customer.grid(row=2, column=0)
   btn_get_customer.grid(row=2, column=1)

#

   lbl_new_customer = Label(customer_app, text='Добавить нового customer', font=font)

   lbl_new_customer_first_name = Label(customer_app, text='Введите first_name нового customer', font=font)
   entry_new_customer_first_name_data = Entry(customer_app, font=font, textvariable=new_customer_first_name)

   lbl_new_customer_last_name = Label(customer_app, text='Введите last_name нового customer', font=font)
   entry_new_customer_last_name_data = Entry(customer_app, font=font, textvariable=new_customer_last_name)

   lbl_new_customer_email = Label(customer_app, text='Введите email нового customer', font=font)
   entry_new_customer_email_data = Entry(customer_app, font=font, textvariable=new_customer_email)

   lbl_new_customer_phone_number = Label(customer_app, text='Введите phone_number нового customer', font=font)
   entry_new_customer_phone_number_data = Entry(customer_app, font=font, textvariable=new_customer_phone_number)

#

   btn_new_customer = Button(customer_app, text='Создать', font=font, command=lambda: fun_new_customer(entry_new_customer_first_name_data.get(),entry_new_customer_last_name_data.get(),entry_new_customer_email_data.get(),entry_new_customer_phone_number_data.get()))
   lbl_new_customer.grid(row=3, column=1)

   lbl_new_customer_first_name.grid(row=4, column=0)
   entry_new_customer_first_name_data.grid(row=4, column=2)

   lbl_new_customer_last_name.grid(row=5, column=0)
   entry_new_customer_last_name_data.grid(row=5, column=2)

   lbl_new_customer_email.grid(row=6, column=0)
   entry_new_customer_email_data.grid(row=6, column=2)

   lbl_new_customer_phone_number.grid(row=7, column=0)
   entry_new_customer_phone_number_data.grid(row=7, column=2)

   btn_new_customer.grid(row=8, column=1)

#

   lbl_upd_customer = Label(customer_app, text='Обновить customer по id', font=font)

   lbl_upd_customer_id = Label(customer_app, text='Введите customer_id', font=font)
   entry_upd_customer = Entry(customer_app, font=font, textvariable=upd_id)

   lbl_upd_customer_first_name = Label(customer_app, text='Введите first_name customer', font=font)
   entry_upd_customer_first_name_data = Entry(customer_app, font=font, textvariable=upd_customer_first_name)

   lbl_upd_customer_last_name = Label(customer_app, text='Введите last_name customer', font=font)
   entry_upd_customer_last_name_data = Entry(customer_app, font=font, textvariable=upd_customer_last_name)

   lbl_upd_customer_email = Label(customer_app, text='Введите email customer', font=font)
   entry_upd_customer_email_data = Entry(customer_app, font=font, textvariable=upd_customer_email)

   lbl_upd_customer_phone_number = Label(customer_app, text='Введите phone_number customer', font=font)
   entry_upd_customer_phone_number_data = Entry(customer_app, font=font, textvariable=upd_customer_phone_number)

#

   btn_upd_customer = Button(customer_app, text='Обновить', font=font, command=lambda: fun_upd_customer(entry_upd_customer.get(),entry_upd_customer_first_name_data.get(),entry_upd_customer_last_name_data.get(),entry_upd_customer_email_data.get(),entry_upd_customer_phone_number_data.get()))
   lbl_upd_customer.grid(row=9, column=1)

   lbl_upd_customer_id.grid(row=10, column=0)
   entry_upd_customer.grid(row=10, column=2)

   lbl_upd_customer_first_name.grid(row=11, column=0)
   entry_upd_customer_first_name_data.grid(row=11, column=2)

   lbl_upd_customer_last_name.grid(row=12, column=0)
   entry_upd_customer_last_name_data.grid(row=12, column=2)

   lbl_upd_customer_email.grid(row=13, column=0)
   entry_upd_customer_email_data.grid(row=13, column=2)

   lbl_upd_customer_phone_number.grid(row=14, column=0)
   entry_upd_customer_phone_number_data.grid(row=14, column=2)

   btn_upd_customer.grid(row=15, column=1)

#

   lbl_del_customer = Label(customer_app, text='Удалить customer по id', font=font)
   entry_del_customer = Entry(customer_app, font=font, textvariable=del_id)
   btn_del_customer = Button(customer_app, text='Удалить', font=font, command=lambda: fun_del_customer(entry_del_customer.get()))

   lbl_del_customer.grid(row=16, column=1)
   entry_del_customer.grid(row=17, column=0)
   btn_del_customer.grid(row=17, column=1)


#
   global lb2_response
   lb1_response = Label(customer_app, text='Полученный ответ', font=font)
   lb2_response = Label(customer_app, text='', font=font)

   lb1_response.grid(row=18, column=1)
   lb2_response.grid(row=19, column=1)

def get_response(s):
   response = s
   print(response)
   lb2_response.config(text=response)

#

def fun_get_customer(customer_id):
   r = requests.get(f'http://127.0.0.1:8000/customers/{customer_id}')
   answer = r.json()
   get_response(answer)

def fun_new_customer(first_name,last_name,email,phone_number):
   data = f'{{ "first_name": "{first_name}", "last_name": "{last_name}", "email": "{email}", "phone_number": "{phone_number}"}}'
   r = requests.post(f'http://127.0.0.1:8000/customers/',data=data)
   answer = r.json()
   get_response(answer)

def fun_upd_customer(customer_id,first_name,last_name,email,phone_number):
   data = f'{{ "first_name": "{first_name}", "last_name": "{last_name}", "email": "{email}", "phone_number": "{phone_number}" }}'
   r = requests.put(f'http://127.0.0.1:8000/customers/{customer_id}',data=data)
   answer = r.json()
   get_response(answer)

def fun_del_customer(customer_id):
   r = requests.delete(f'http://127.0.0.1:8000/customers/{customer_id}')
   answer = r.json()
   get_response(answer)