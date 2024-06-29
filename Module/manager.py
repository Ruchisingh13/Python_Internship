employe_name = "rocky"
employe_id = "rocky@gmail.com"
employe_pass = "rocky@12345"
employe_salary = 80000

if __name__ == "__main__":
    manager_name = "ramesh chandra"
    manager_id = "hello@gmail.com"
    manager_pass = "helo@12345"
    manager_salary = 80000

def avg_finder(ls):
    total_sum = 0
    count = 0
    for item in ls:
        total_sum += item
        count += 1
    average = total_sum/count
    print("Your average is :",round(average,2))    
    
print("manager file executed!")    