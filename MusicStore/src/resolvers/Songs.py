from sql_base.base import base_worker
from sql_base.models import SongsM

def get_Song(Song_id) -> int:
    get_Song1 = base_worker.insert_data(f"SELECT * FROM Song WHERE id = {Song_id}",())
    return get_Song1

def new_Song(Song: SongsM) -> int:
    new_id = base_worker.insert_data(f"""INSERT INTO Song (left_in_stock, note) 
                                    VALUES(?,?) RETURNING id;""",
                                    (Song.left_in_stock, Song.note))
    return new_id
# 
def upd_Song(Song_id,Song: SongsM) -> int:
    upd_id = base_worker.insert_data(f"""UPDATE Song SET left_in_stock=(?), note=(?) WHERE id = {Song_id} RETURNING id;""",
                                     (Song.left_in_stock, Song.note))
    return upd_id

def del_Song(Song_id) -> int:
    del_id = base_worker.insert_data(f"DELETE FROM Song WHERE id = {Song_id} RETURNING id;",())
    return del_id