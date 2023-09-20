#Define a function that accepts 2 values and return its sum, subtraction and multiplication.

def sum(a,b):
    sum = a+b
    print("Sum of" , a , "and" , b , "is" , sum)

def subtraction(a,b):
    subtraction = a-b
    print("Subtraction of" , a , "and" , b , "is" , subtraction)

def multiplication(a,b):
    multiplication = a*b
    print("Multiplication of" , a , "and" , b , "is" , multiplication)

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

sum(num1,num2)
subtraction(num1,num2)
multiplication(num1,num2)