from sql_base.models import usersM
from sql_base.base import base_worker

def check_login_request(user: usersM):
    post_id = base_worker.insert_data(f"SELECT id FROM user WHERE username = ? AND password = ?",(user.username,user.password))
    return post_id
