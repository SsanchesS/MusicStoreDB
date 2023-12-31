from fastapi import APIRouter
from sql_base.models import EmployeesM
import resolvers.Employees

Employees_router = APIRouter()

@Employees_router.get('/{employee_id}')
def get_Employee(employee_id: int):
    employee = resolvers.Employees.get_Employee(employee_id)
    if employee is None:
        return {"code": 404, 'message': f"Employee with id {employee_id} not found"}
    return {"code": 201, "Employee": employee}

@Employees_router.post('/')
def new_Employee(employee: EmployeesM):
    new_id = resolvers.Employees.new_Employee(employee)
    return {"code": 201, "id": new_id}

@Employees_router.put('/{employee_id}')
def update_Employee(employee_id: int, employee: EmployeesM):
    upd_id = resolvers.Employees.upd_Employee(employee_id, employee)
    if upd_id is None:
       return {"code": 404, 'message': f"Employee with id {employee_id} not found"}
    return {"code": 201, "Update Employee": upd_id}

@Employees_router.delete('/{employee_id}')
def delete_Employee(employee_id: int):
    del_id = resolvers.Employees.del_Employee(employee_id)
    if del_id is None:
       return {"code": 404, 'message': f"Employee with id {employee_id} not found"}
    return {"code": 201, "Delete Employee": del_id}