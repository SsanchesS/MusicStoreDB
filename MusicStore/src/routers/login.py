from fastapi import APIRouter, HTTPException
from sql_base.models import CustomersM
from resolvers.check_login import check_login_request

login_router = APIRouter()

@login_router.get('/')
def not_login():
    return {"Message": "Login in system"}

@login_router.post('/log')
def check_login1(user: CustomersM):
    user_id = check_login_request(user)
    if user_id:
        return {"code": 200, "message": "Login correct", 'user_id': user_id}
    else:
        raise HTTPException(status_code=401, detail="Login incorrect, try again")