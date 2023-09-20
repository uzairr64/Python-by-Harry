#Define a function that accepts 2 values and return its sum, subtraction and multiplication.
def function(a,b):
    if want == "sum":
        sum = a + b
        print("Sum of" , a , "and" , b , "is" , sum)

    elif want == "subtraction":
        subtraction = a - b
        print("Subtraction of" , a , "and" , b , "is" ,subtraction)

    else:
        multipliction = a * b
        print("Multiplication of" , a , "and" , b , "is" ,multipliction)  

num1 = int(input("enter First Number:"))
num2 = int(input("enter Second Number:"))
want = input("What Do You Want?")

function(num1 , num2)
