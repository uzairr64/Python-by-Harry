#Define a function in python that accepts 3 values and returns the maximum of three numbers.

def function(a,b,c):
    if a>b and a>c:
        print("a is Maximum >>>" , a)
    
    elif b>a and b>c:
        print("b is Maximum >>>" , b)
        
    elif c>a and c>b:
        print("c is Maximum >>>" , c)
        
    else:
        print("All Numbers are Equal!")
        
num1 = int(input("enter First Number: "))
num2 = int(input("enter Second Number: "))
num3 = int(input("enter Third Number: "))

function(num1,num2,num3)