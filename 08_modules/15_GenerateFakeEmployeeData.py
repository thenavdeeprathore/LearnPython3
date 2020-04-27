"""
1) Employee name should contain 3 to 10 characters
    First character should be Upper-case and remaining lower-case
2) Employee number should starts with "e-" followed by 4 digits
3) Employee salary should be float value from 10000 to 50000
4) Employee city should be from ['tokyo', 'london', 'paris', 'sweden', 'pune']
5) Mobile number should contain exactly 10 digits where first number should be
    6 to 9 and no restriction on remaining digits
6) Employee designation should be from:
    ['Software Engineer', 'Senior Software Engineer', 'Team Lead', 'Project Manager']

"""

from random import *

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
cities = ['Tokyo', 'London', 'Paris', 'Sweden', 'Pune']
designations = ['Software Engineer', 'Senior Software Engineer', 'Team Lead', 'Project Manager']


def get_fake_name():
    """
    This function generates fake employee name
        - Employee name should contain 3 to 10 characters
        - First character should be Upper-case and remaining lower-case
    """
    name = choice(alphabets).upper()
    n = randint(2, 9)
    for i in range(n):
        name = name + choice(alphabets)
    return name


def get_fake_eno():
    """
    This function generates fake employee number
        - Employee number should starts with "e-" followed by 4 digits
    """
    eno = "e-"
    for i in range(4):
        eno = eno + choice(digits)
    return eno


def get_fake_emp_sal():
    """
    This function generates fake employee salary
        - Employee salary should be float value
        - Salary range from 10000 to 50000
    """
    emp_sal = uniform(10000, 50000)
    return emp_sal


def get_fake_city():
    """
    This function generates fake employee city
        - Employee city should be from ['tokyo', 'london', 'paris', 'sweden', 'pune']
    """
    city = choice(cities)
    return city


def get_fake_mobile_number():
    """
    This function generates fake employee mobile number
        - Mobile number should contain exactly 10 digits where first number should be
        - 6 to 9 and no restriction on remaining digits
    """
    mobile_number = choice('6789')
    for i in range(9):
        mobile_number = mobile_number + choice(digits)
    return mobile_number


def get_fake_designation():
    """
    This function generates fake employee designation
        - ['Software Engineer', 'Senior Software Engineer', 'Team Lead', 'Project Manager']
    """
    designation = choice(designations)
    return designation


def get_fake_employee_data():
    print("Employee Name: ", get_fake_name())
    print("Employee Id Number: ", get_fake_eno())
    print("Employee Salary: {:.2f}".format(get_fake_emp_sal()))
    print("Employee City: ", get_fake_city())
    print("Employee Mobile Number: ", get_fake_mobile_number())
    print("Employee Designation: ", get_fake_designation())


for i in range(5):
    get_fake_employee_data()
    print("------------------")

