from sql_base.base import base_worker
from sql_base.models import EmployeesM

def get_Employee(employee_id) -> str:
    get_Employee1 = base_worker.insert_data(f"SELECT * FROM Employees WHERE employee_id = {employee_id}",())
    return get_Employee1

def new_Employee(employee: EmployeesM) -> str:
    new_employee_id = base_worker.insert_data(f"""
        INSERT INTO Employees (first_name, last_name, hire_date, position) 
        VALUES (?, ?, ?, ?) RETURNING employee_id;
    """, (employee.first_name, employee.last_name, employee.hire_date, employee.position))
    return new_employee_id

def upd_Employee(employee_id, employee: EmployeesM) -> str:
    upd_employee_id = base_worker.insert_data(f"""
        UPDATE Employees 
        SET first_name = ?, last_name = ?, hire_date = ?, position = ?
        WHERE employee_id = {employee_id} 
        RETURNING employee_id;
    """, (employee.first_name, employee.last_name, employee.hire_date, employee.position))
    return upd_employee_id

def del_Employee(employee_id) -> str:
    del_employee_id = base_worker.insert_data(f"DELETE FROM Employees WHERE employee_id = {employee_id} RETURNING employee_id;",())
    return del_employee_id