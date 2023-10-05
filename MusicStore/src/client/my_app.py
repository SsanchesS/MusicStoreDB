from tkinter import *
from  user_api import create_user_app
from  manager_api import create_manager_app

def create_app(root,font):
    app = Toplevel(root)
    app.title("Выберите запрос")  
    app.geometry('200x100')

    def create_app_user():
      app.withdraw()
      create_user_app(root,font)

    def create_app_manager():
      app.withdraw()
      create_manager_app(root,font)

    btn_app_user = Button(app, text='user', font=font, command=create_app_user)
    btn_app_manager = Button(app, text='manager', font=font, command=create_app_manager)

    btn_app_user.grid(row=0, column=0)
    btn_app_manager.grid(row=0, column=2)



