from sql_base.base import base_worker
from sql_base.models import PublishersM

def get_Publisher(publisher_id) -> int:
    get_Publisher1 = base_worker.insert_data(f"SELECT * FROM Publishers WHERE publisher_id = {publisher_id}",())
    return get_Publisher1

def new_Publisher(publisher: PublishersM) -> int:
    new_publisher_id = base_worker.insert_data(f"""
        INSERT INTO Publishers (name, country) 
        VALUES (?, ?) RETURNING publisher_id;
    """, (publisher.name, publisher.country))
    return new_publisher_id

def upd_Publisher(publisher_id, publisher: PublishersM) -> int:
    upd_publisher_id = base_worker.insert_data(f"""
        UPDATE Publishers 
        SET name = ?, country = ?
        WHERE publisher_id = {publisher_id} 
        RETURNING publisher_id;
    """, (publisher.name, publisher.country))
    return upd_publisher_id

def del_Publisher(publisher_id) -> int:
    del_publisher_id = base_worker.insert_data(f"DELETE FROM Publishers WHERE publisher_id = {publisher_id} RETURNING publisher_id;",())
    return del_publisher_id