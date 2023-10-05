from sql_base.base import base_worker
from sql_base.models import PublishersM

def get_Publisher(Publisher_id) -> int:
    get_Publisher1 = base_worker.insert_data(f"SELECT * FROM Publisher WHERE id = {Publisher_id}",())
    return get_Publisher1

def new_Publisher(Publisher: PublishersM) -> int:
    new_id = base_worker.insert_data(f"""INSERT INTO Publisher (left_in_stock, note) 
                                    VALUES(?,?) RETURNING id;""",
                                    (Publisher.left_in_stock, Publisher.note))
    return new_id
# 
def upd_Publisher(Publisher_id,Publisher: PublishersM) -> int:
    upd_id = base_worker.insert_data(f"""UPDATE Publisher SET left_in_stock=(?), note=(?) WHERE id = {Publisher_id} RETURNING id;""",
                                     (Publisher.left_in_stock, Publisher.note))
    return upd_id

def del_Publisher(Publisher_id) -> int:
    del_id = base_worker.insert_data(f"DELETE FROM Publisher WHERE id = {Publisher_id} RETURNING id;",())
    return del_id