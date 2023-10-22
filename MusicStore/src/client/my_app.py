from tkinter import *
from  api.albums_api import create_album_app
from  api.artists_api import create_artist_app
from  api.genres_api import create_genres_app
from  api.songs_api import create_songs_app
from  api.customer_api import create_customer_app
from  api.orders_api import create_orders_app
from  api.orderDetails_api import create_orderDetails_app
from  api.employees_api import create_employees_app
from  api.publishers_api import create_publishers_app
from  api.copyrights_api import create_copyrights_app

def create_app(root,font,customer_id_props):
  app = Toplevel(root)
  app.title("Выберите запрос")  
  app.geometry('400x250')

  def create_app_albums():
    app.withdraw()
    create_album_app(root,font)
  
  def create_app_artists():
    app.withdraw()
    create_artist_app(root,font)

  def create_app_genres():
    app.withdraw()
    create_genres_app(root,font)

  def create_app_songs():
    app.withdraw()
    create_songs_app(root,font)

  def create_app_customer():
    app.withdraw()
    create_customer_app(root,font,customer_id_props)

  def create_app_orders():
    app.withdraw()
    create_orders_app(root,font)

  def create_app_orderDetails():
    app.withdraw()
    create_orderDetails_app(root,font)

  def create_app_employees():
    app.withdraw()
    create_employees_app(root,font)

  def create_app_publishers():
    app.withdraw()
    create_publishers_app(root,font)

  def create_app_copyrights():
    app.withdraw()
    create_copyrights_app(root,font)
    

  btn_app_albums = Button(app, text='albums', font=font, command=create_app_albums)

  btn_app_albums.grid(row=1, column=0)

  btn_app_artists = Button(app, text='artists', font=font, command=create_app_artists)

  btn_app_artists.grid(row=1, column=1)

  btn_app_genres = Button(app, text='genres', font=font, command=create_app_genres)

  btn_app_genres.grid(row=2, column=0)

  btn_app_songs = Button(app, text='songs', font=font, command=create_app_songs)

  btn_app_songs.grid(row=2, column=1)

  btn_app_customer = Button(app, text='customer', font=font, command=create_app_customer)

  btn_app_customer.grid(row=3, column=0)

  btn_app_orders = Button(app, text='orders', font=font, command=create_app_orders)

  btn_app_orders.grid(row=3, column=1)

  btn_app_orderDetails = Button(app, text='orderDetails', font=font, command=create_app_orderDetails)

  btn_app_orderDetails.grid(row=4, column=0)

  btn_app_employees = Button(app, text='employees', font=font, command=create_app_employees)

  btn_app_employees.grid(row=4, column=1)

  btn_app_publishers = Button(app, text='publishers', font=font, command=create_app_publishers)

  btn_app_publishers.grid(row=5, column=0)

  btn_app_copyrights = Button(app, text='copyrights', font=font, command=create_app_copyrights)

  btn_app_copyrights.grid(row=5, column=1)