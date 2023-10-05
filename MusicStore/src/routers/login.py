from fastapi import APIRouter
from sql_base.models import usersM
from resolvers.check_login import check_login_request

login_router = APIRouter()


@login_router.get('/')
def not_login():
    return {"Message": "Login in system"}

@login_router.post('/log')
def check_login1(user: usersM):
    id = check_login_request(user)
    if id:
        return {"code": 200, "message": "Login correct", 'id': id}
    else:
        return {"code": 401, "message": "Login incorrect, try again", 'id': None}