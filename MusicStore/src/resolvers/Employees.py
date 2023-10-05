from sql_base.base import base_worker
from sql_base.models import EmployeesM

def get_Employee(Employee_id) -> str:
    get_Employee1 = base_worker.insert_data(f"SELECT * FROM Employee_table WHERE id = {Employee_id}",())
    return get_Employee1

def new_Employee(Employee1: EmployeesM) -> str:
    new_Employee1 = base_worker.insert_data(f"""INSERT INTO Employee_table (Employee, note) 
                                    VALUES(?,?) RETURNING id;""",
                                    (Employee1.Employee, Employee1.note))
    return new_Employee1
# 
def upd_Employee(Employee_id,Employee1: EmployeesM) -> str:
    upd_Employee1 = base_worker.insert_data(f"""UPDATE Employee_table SET Employee=(?), note=(?) WHERE id = {Employee_id} RETURNING id;""",
                                     (Employee1.Employee, Employee1.note))
    return upd_Employee1

def del_Employee(Employee_id) -> str:
    del_Employee1 = base_worker.insert_data(f"DELETE FROM Employee_table WHERE id = {Employee_id} RETURNING id;",())
    return del_Employee1