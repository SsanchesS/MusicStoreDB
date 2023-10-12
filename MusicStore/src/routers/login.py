from fastapi import APIRouter
from sql_base.models import LoginM
from resolvers.check_login import check_login_request

login_router = APIRouter()

@login_router.post('/')
def check_login_response(customer:LoginM):
    customer_id = check_login_request(customer)
    if customer_id:
        return {"code": 200, "message": "Login correct", 'customer_id': customer_id}
    else:
        return {"code": 401, "message": "Login incorrect, try again"}