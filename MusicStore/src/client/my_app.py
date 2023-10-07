from tkinter import *
from  customer_api import create_customer_app

def create_app(root,font):
  app = Toplevel(root)
  app.title("Выберите запрос")  
  app.geometry('200x100')

  def create_app_customer():
    app.withdraw()
    create_customer_app(root,font)

  btn_app_customer = Button(app, text='customer', font=font, command=create_app_customer)

  btn_app_customer.grid(row=0, column=0)