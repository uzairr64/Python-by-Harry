salary = int(input("enter Salary: "))
service = int(input("enter your years of service: "))

#print("Emplyee Salary is: " , salaray)
#print("Emplyee Year of Service is: " , service)

if service > 5:
    bonus = (salary*5)/100
    salary = salary+bonus
    print(salary)

elif service < 5:
    print(salary)
    
else:
    print(salary)    
    
   