import requests
from tkinter import *

def create_artist_app(root,font):
   artist_app = Toplevel(root)
   artist_app.title("Работа с artists")  
   artist_app.geometry('1400x700')


   get_id = StringVar()
   upd_id = StringVar()
   del_id = StringVar()

   new_artist_name = StringVar()
   upd_artist_name = StringVar()

   new_artist_country = StringVar()
   upd_artist_country = StringVar()

   new_artist_active_years = StringVar()
   upd_artist_active_years = StringVar()


#

   lbl_get_artist = Label(artist_app, text="Показать artist по id", font=font)
   entry_get_artist = Entry(artist_app, font=font, textvariable=get_id)
   btn_get_artist = Button(artist_app, text='Получить', font=font, command=lambda: fun_get_artist(entry_get_artist.get()))
   lbl_get_artist.grid(row=1, column=1)
   entry_get_artist.grid(row=2, column=0)
   btn_get_artist.grid(row=2, column=1)

#

   lbl_new_artist = Label(artist_app, text='Добавить нового artist', font=font)

   lbl_new_artist_name = Label(artist_app, text='Введите name нового artist', font=font)
   entry_new_artist_name_data = Entry(artist_app, font=font, textvariable=new_artist_name)

   lbl_new_artist_country= Label(artist_app, text='Введите country нового artist', font=font)
   entry_new_artist_country_data = Entry(artist_app, font=font, textvariable=new_artist_country)

   lbl_new_artist_active_years = Label(artist_app, text='Введите active_years нового artist', font=font)
   entry_new_artist_active_years_data = Entry(artist_app, font=font, textvariable=new_artist_active_years)

#

   btn_new_artist = Button(artist_app, text='Создать', font=font, command=lambda: fun_new_artist(entry_new_artist_name_data.get(),entry_new_artist_country_data.get(),entry_new_artist_active_years_data.get()))
   lbl_new_artist.grid(row=3, column=1)

   lbl_new_artist_name.grid(row=4, column=0)
   entry_new_artist_name_data.grid(row=4, column=2)

   lbl_new_artist_country.grid(row=5, column=0)
   entry_new_artist_country_data.grid(row=5, column=2)

   lbl_new_artist_active_years.grid(row=6, column=0)
   entry_new_artist_active_years_data.grid(row=6, column=2)


   btn_new_artist.grid(row=7, column=1)

#

   lbl_upd_artist = Label(artist_app, text='Обновить artist по id', font=font)

   lbl_upd_artist_id = Label(artist_app, text='Введите artist_id', font=font)
   entry_upd_artist = Entry(artist_app, font=font, textvariable=upd_id)

   lbl_upd_artist_name = Label(artist_app, text='Введите name artist', font=font)
   entry_upd_artist_name_data = Entry(artist_app, font=font, textvariable=upd_artist_name)

   lbl_upd_artist_country = Label(artist_app, text='Введите country artist', font=font)
   entry_upd_artist_country_data = Entry(artist_app, font=font, textvariable=upd_artist_country)

   lbl_upd_artist_active_years = Label(artist_app, text='Введите active_years artist', font=font)
   entry_upd_artist_active_years_data = Entry(artist_app, font=font, textvariable=upd_artist_active_years)


#

   btn_upd_artist = Button(artist_app, text='Обновить', font=font, command=lambda: fun_upd_artist(entry_upd_artist.get(),entry_upd_artist_name_data.get(),entry_upd_artist_country_data.get(),entry_upd_artist_active_years_data.get()))
   lbl_upd_artist.grid(row=8, column=1)

   lbl_upd_artist_id.grid(row=9, column=0)
   entry_upd_artist.grid(row=9, column=2)

   lbl_upd_artist_name.grid(row=10, column=0)
   entry_upd_artist_name_data.grid(row=10, column=2)

   lbl_upd_artist_country.grid(row=11, column=0)
   entry_upd_artist_country_data.grid(row=11, column=2)

   lbl_upd_artist_active_years.grid(row=12, column=0)
   entry_upd_artist_active_years_data.grid(row=12, column=2)


   btn_upd_artist.grid(row=13, column=1)

#

   lbl_del_artist = Label(artist_app, text='Удалить artist по id', font=font)
   entry_del_artist = Entry(artist_app, font=font, textvariable=del_id)
   btn_del_artist = Button(artist_app, text='Удалить', font=font, command=lambda: fun_del_artist(entry_del_artist.get()))

   lbl_del_artist.grid(row=14, column=1)
   entry_del_artist.grid(row=15, column=0)
   btn_del_artist.grid(row=15, column=1)


#
   global lb2_response
   lb1_response = Label(artist_app, text='Полученный ответ', font=font)
   lb2_response = Label(artist_app, text='', font=font)

   lb1_response.grid(row=16, column=1)
   lb2_response.grid(row=17, column=1)

def get_response(s):
   response = s
   print(response)
   lb2_response.config(text=response)

#

def fun_get_artist(artist_id):
   r = requests.get(f'http://127.0.0.1:8000/artists/{artist_id}')
   answer = r.json()
   get_response(answer)

def fun_new_artist(name,country,active_years):
   data = f'{{ "name": "{name}", "country": "{country}", "active_years": "{active_years}"}}'
   r = requests.post(f'http://127.0.0.1:8000/artists/',data=data)
   answer = r.json()
   get_response(answer)

def fun_upd_artist(artist_id,name,country,active_years):
   data = f'{{ "name": "{name}", "country": "{country}", "active_years": "{active_years}"}}'
   r = requests.put(f'http://127.0.0.1:8000/artists/{artist_id}',data=data)
   answer = r.json()
   get_response(answer)

def fun_del_artist(artist_id):
   r = requests.delete(f'http://127.0.0.1:8000/artists/{artist_id}')
   answer = r.json()
   get_response(answer)