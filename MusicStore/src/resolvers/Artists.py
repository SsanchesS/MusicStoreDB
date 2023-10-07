from sql_base.base import base_worker
from sql_base.models import ArtistsM

def get_Artist(artist_id) -> int:
    get_artist = base_worker.insert_data(f"SELECT * FROM Artists WHERE artist_id = {artist_id}",())
    return get_artist

def new_Artist(artist: ArtistsM) -> int:
    new_id = base_worker.insert_data(f"""
        INSERT INTO Artists (name, country, active_years) 
        VALUES (?, ?, ?) RETURNING artist_id;
    """, (artist.name, artist.country, artist.active_years))
    return new_id

def upd_Artist(artist_id, artist: ArtistsM) -> int:
    upd_id = base_worker.insert_data(f"""
        UPDATE Artists 
        SET name = ?, country = ?, active_years = ?
        WHERE artist_id = {artist_id} 
        RETURNING artist_id;
    """, (artist.name, artist.country, artist.active_years))
    return upd_id

def del_Artist(artist_id) -> int:
    del_id = base_worker.insert_data(f"DELETE FROM Artists WHERE artist_id = {artist_id} RETURNING artist_id;",())
    return del_id