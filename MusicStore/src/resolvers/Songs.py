from sql_base.base import base_worker
from sql_base.models import SongsM

def get_Song(song_id) -> str:
    get_song = base_worker.insert_data(f"SELECT * FROM Songs WHERE song_id = {song_id}",())
    return get_song

def new_Song(song: SongsM) -> str:
    new_song_id = base_worker.insert_data(f"""
        INSERT INTO Songs (title, album_id, artist_id, duration) 
        VALUES (?, ?, ?, ?) RETURNING song_id;
    """, (song.title, song.album_id, song.artist_id, song.duration))
    return new_song_id

def upd_Song(song_id, song: SongsM) -> str:
    upd_song_id = base_worker.insert_data(f"""
        UPDATE Songs 
        SET title = ?, album_id = ?, artist_id = ?, duration = ?
        WHERE song_id = {song_id} 
        RETURNING song_id;
    """, (song.title, song.album_id, song.artist_id, song.duration))
    return upd_song_id

def del_Song(song_id) -> str:
    del_song_id = base_worker.insert_data(f"DELETE FROM Songs WHERE song_id = {song_id} RETURNING song_id;",())
    return del_song_id