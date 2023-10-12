from fastapi import APIRouter
from sql_base.models import CustomersM
import resolvers.Customers

Customers_router = APIRouter()

@Customers_router.get('/{customer_id}')
def get_Customer(customer_id: int):
    customer = resolvers.Customers.get_Customer(customer_id)
    if customer is None:
        return {"code": 404, 'message': f"Customer with id {customer_id} not found"}
    return {"code": 201, 'Customer': customer}

@Customers_router.post('/')
def new_Customer(customer: CustomersM):
    new_id = resolvers.Customers.new_Customer(customer)
    return {"code": 201, "id": new_id}

@Customers_router.put('/{customer_id}')
def update_Customer(customer_id: int, customer: CustomersM):
    upd_id = resolvers.Customers.upd_Customer(customer_id, customer)
    if upd_id is None:
        return {"code": 404, 'message': f"Customer with id {customer_id} not found"}
    return {"code": 201, "Update Customer": upd_id}

@Customers_router.delete('/{customer_id}')
def delete_Customer(customer_id: int):
    del_id = resolvers.Customers.del_Customer(customer_id)
    if del_id is None:
        return {"code": 404, 'message': f"Customer with id {customer_id} not found"}
    return {"code": 201, "Delete Customer": del_id}