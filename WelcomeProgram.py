"""
This program is created for exploring all concepts in python
"""
city="hyderabad"
global salary
salary ="100"
def checkSalary(salary,message):
    salary=int(salary)
    a = 10
    if 10 < 3:
        print("This is my first python program using Git and salary =",salary)
    else:
        print("This is my second python program using Git",salary,type(salary),message)
        print("this is for testing pull from remote master to local")

checkSalary(salary,"this is message")
