from sql_base.base import base_worker
from sql_base.models import GenresM

def get_Genre(genre_id) -> str:
    get_genre = base_worker.insert_data(f"SELECT * FROM Genres WHERE genre_id = {genre_id}",())
    return get_genre

def new_Genre(genre: GenresM) -> str:
    new_genre_id = base_worker.insert_data(f"""
        INSERT INTO Genres (name) 
        VALUES (?) RETURNING genre_id;
    """, (genre.name,))
    return new_genre_id

def upd_Genre(genre_id, genre: GenresM) -> str:
    upd_genre_id = base_worker.insert_data(f"""
        UPDATE Genres 
        SET name = ?
        WHERE genre_id = {genre_id} 
        RETURNING genre_id;
    """, (genre.name,))
    return upd_genre_id

def del_Genre(genre_id) -> str:
    del_genre_id = base_worker.insert_data(f"DELETE FROM Genres WHERE genre_id = {genre_id} RETURNING genre_id;",())
    return del_genre_id