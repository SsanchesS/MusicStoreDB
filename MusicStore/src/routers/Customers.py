from fastapi import APIRouter
from sql_base.models import CustomersM
import resolvers.Customers

Customers_router = APIRouter()

@Customers_router.get('/')
def get_Customer():
    return f'Response: {{text: Страница со списком Customers}}'

@Customers_router.get('/{Customer_id}')
def get_Customer(Customer_id: int):
    get_Customer1 = resolvers.Customers.get_Customer(Customer_id)
    return f'Customer: {get_Customer1}'

@Customers_router.post('/')
def new_Customer(Customer: CustomersM):
    new_id = resolvers.Customers.new_Customer(Customer)
    return f'{{code: 201, id: {new_id}}}'

@Customers_router.put('/{Customer_id}')
def update_Customer(Customer_id:int,Customer: CustomersM):
    upd_id = resolvers.Customers.upd_Customer(Customer_id,Customer)
    return f'Update Customer {upd_id}'

@Customers_router.delete('/{Customer_id}')
def delelte_Customer(Customer_id: int):
    del_id = resolvers.Customers.del_Customer(Customer_id)
    return f'Delete Customer {del_id}'