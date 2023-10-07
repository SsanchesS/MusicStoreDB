from sql_base.base import base_worker
from sql_base.models import AlbumsM

def get_Album(album_id):
    get_album = base_worker.insert_data(f"SELECT * FROM Albums WHERE album_id = {album_id}",())
    return get_album

def new_Album(album: AlbumsM) -> int:
    new_id = base_worker.insert_data(f"""
        INSERT INTO Albums (title, artist_id, release_date, genre_id) 
        VALUES (?, ?, ?, ?) RETURNING album_id;
    """, (album.title, album.artist_id, album.release_date, album.genre_id))
    return new_id
# 
def upd_Album(album_id, album: AlbumsM) -> int:
    upd_id = base_worker.insert_data(f"""
        UPDATE Albums 
        SET title = ?, artist_id = ?, release_date = ?, genre_id = ?
        WHERE album_id = {album_id} 
        RETURNING album_id;
    """, (album.title, album.artist_id, album.release_date, album.genre_id))
    return upd_id

def del_Album(album_id) -> int:
    del_id = base_worker.insert_data(f"DELETE FROM Albums WHERE album_id = {album_id} RETURNING album_id;",())
    return del_id