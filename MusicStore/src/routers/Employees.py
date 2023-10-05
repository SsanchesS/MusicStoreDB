from fastapi import APIRouter
from sql_base.models import EmployeesM
import resolvers.Employees

Employees_router = APIRouter()

@Employees_router.get('/')
def get_Employee():
    return f'Response: {{text: Страница со списком Employees}}'

@Employees_router.get('/{Employee_id}')
def get_Employee(Employee_id: int):
    get_Employee1 = resolvers.Employees.get_Employee(Employee_id)
    return f'Employee: {get_Employee1}'

@Employees_router.post('/')
def new_Employee(Employee: EmployeesM):
    new_id = resolvers.Employees.new_Employee(Employee)
    return f'{{code: 201, id: {new_id}}}'

@Employees_router.put('/{Employee_id}')
def update_Employee(Employee_id:int,Employee: EmployeesM):
    upd_id = resolvers.Employees.upd_Employee(Employee_id,Employee)
    return f'Update Employee {upd_id}'

@Employees_router.delete('/{Employee_id}')
def delelte_Employee(Employee_id: int):
    del_id = resolvers.Employees.del_Employee(Employee_id)
    return f'Delete Employee {del_id}'