from sql_base.base import base_worker
from sql_base.models import ArtistsM

def get_Artist(Artist_id) -> int:
    get_Artist1 = base_worker.insert_data(f"SELECT * FROM Artist WHERE id = {Artist_id}",())
    return get_Artist1

def new_Artist(Artist: ArtistsM) -> int:
    new_id = base_worker.insert_data(f"""INSERT INTO Artist (title, short_name) 
                                    VALUES(?,?) RETURNING id;""",
                                    (Artist.title, Artist.short_name))
    return new_id
# 
def upd_Artist(Artist_id,Artist: ArtistsM) -> int:
    upd_id = base_worker.insert_data(f"""UPDATE Artist SET title=(?), short_name=(?) WHERE id = {Artist_id} RETURNING id;""",
                                     (Artist.title, Artist.short_name))
    return upd_id

def del_Artist(Artist_id) -> int:
    del_id = base_worker.insert_data(f"DELETE FROM Artist WHERE id = {Artist_id} RETURNING id;",())
    return del_id