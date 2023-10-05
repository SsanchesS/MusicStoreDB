from sql_base.base import base_worker
from sql_base.models import GenresM

def get_Genre(Genre_id) -> str:
    get_Genre1 = base_worker.insert_data(f"SELECT * FROM Genre_table WHERE id = {Genre_id}",())
    return get_Genre1

def new_Genre(Genre1: GenresM) -> str:
    new_Genre1 = base_worker.insert_data(f"""INSERT INTO Genre_table (Genre, note) 
                                    VALUES(?,?) RETURNING id;""",
                                    (Genre1.Genre, Genre1.note))
    return new_Genre1
# 
def upd_Genre(Genre_id,Genre1: GenresM) -> str:
    upd_Genre1 = base_worker.insert_data(f"""UPDATE Genre_table SET Genre=(?), note=(?) WHERE id = {Genre_id} RETURNING id;""",
                                     (Genre1.Genre, Genre1.note))
    return upd_Genre1

def del_Genre(Genre_id) -> str:
    del_Genre1 = base_worker.insert_data(f"DELETE FROM Genre_table WHERE id = {Genre_id} RETURNING id;",())
    return del_Genre1