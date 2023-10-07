from sql_base.base import base_worker
from sql_base.models import CopyrightsM

def get_Copyright(copyright_id) -> int:
    get_Copyright1 = base_worker.insert_data(f"SELECT * FROM Copyrights WHERE copyright_id = {copyright_id}",())
    return get_Copyright1

def new_Copyright(copyright: CopyrightsM) -> int:
    new_id = base_worker.insert_data(f"""
        INSERT INTO Copyrights (song_id, publisher_id, royalty_rate) 
        VALUES (?, ?, ?) RETURNING copyright_id;
    """, (copyright.song_id, copyright.publisher_id, copyright.royalty_rate))
    return new_id

def upd_Copyright(copyright_id, copyright: CopyrightsM) -> int:
    upd_id = base_worker.insert_data(f"""
        UPDATE Copyrights 
        SET song_id = ?, publisher_id = ?, royalty_rate = ?
        WHERE copyright_id = {copyright_id} 
        RETURNING copyright_id;
    """, (copyright.song_id, copyright.publisher_id, copyright.royalty_rate))
    return upd_id

def del_Copyright(copyright_id) -> int:
    del_id = base_worker.insert_data(f"DELETE FROM Copyrights WHERE copyright_id = {copyright_id} RETURNING copyright_id;",())
    return del_id