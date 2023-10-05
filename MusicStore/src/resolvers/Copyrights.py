from sql_base.base import base_worker
from sql_base.models import CopyrightsM

def get_Copyright(Copyright_id) -> int:
    get_Copyright1 = base_worker.insert_data(f"SELECT * FROM Copyright WHERE id = {Copyright_id}",())
    return get_Copyright1

def new_Copyright(Copyright: CopyrightsM) -> int:
    new_id = base_worker.insert_data(f"""INSERT INTO Copyright (left_in_stock, note) 
                                    VALUES(?,?) RETURNING id;""",
                                    (Copyright.left_in_stock, Copyright.note))
    return new_id
# 
def upd_Copyright(Copyright_id,Copyright: CopyrightsM) -> int:
    upd_id = base_worker.insert_data(f"""UPDATE Copyright SET left_in_stock=(?), note=(?) WHERE id = {Copyright_id} RETURNING id;""",
                                     (Copyright.left_in_stock, Copyright.note))
    return upd_id

def del_Copyright(Copyright_id) -> int:
    del_id = base_worker.insert_data(f"DELETE FROM Copyright WHERE id = {Copyright_id} RETURNING id;",())
    return del_id