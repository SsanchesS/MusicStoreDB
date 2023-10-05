from sql_base.base import base_worker
from sql_base.models import AlbumsM

def get_Album(Album_id):
    get_Album1 = base_worker.insert_data(f"SELECT * FROM Album WHERE id = {Album_id}",())
    return get_Album1

def new_Album(Album: AlbumsM) -> int:
    new_id = base_worker.insert_data(f"""INSERT INTO Album (user_id) 
                                    VALUES(?) RETURNING id;""",
                                    (Album.user_id,))
    return new_id
# 
def upd_Album(Album_id,Album: AlbumsM) -> int:
    upd_id = base_worker.insert_data(f"""UPDATE Album SET user_id=(?) WHERE id = {Album_id} RETURNING id;""",
                                     (Album.user_id,))
    return upd_id

def del_Album(Album_id) -> int:
    del_id = base_worker.insert_data(f"DELETE FROM Album WHERE id = {Album_id} RETURNING id;",())
    return del_id