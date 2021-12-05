from application import *
from datetime import datetime

if __name__ == '__main__':
    print(f'Today: {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}')
    print(f'Salary: {calculate_salary()}')
    print(f'Employees: {get_employees()}')
