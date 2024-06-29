# import manager

# print("Employee name :",manager.manager_name)
# print("Employee id :",manager.manager_id)
# print("Employee password :",manager.manager_pass)
# print("Employee salary :",manager.manager_salary)



# import manager as mng
# print("Employee name :",mng.manager_name)
# print("Employee id :",mng.manager_id)
# print("Employee password :",mng.manager_pass)
# print("Employee salary :",mng.manager_salary)

# marks = [14,56,78,98,78,65,43,22,2]
# mng.avg_finder(ls=marks)

import manager  # all content recived from the another file

from manager import employe_id,employe_name,employe_pass,employe_salary
from manager import manager_name,manager_id,manager_pass,manager_salary
print()
print("manager name:",employe_name)
print("manager id:",employe_id)
print("manager pass:",employe_pass)
print("manager salary:",employe_salary)

print()

print(manager_name)
print(manager_id)
print(manager_pass)
print(manager_salary)