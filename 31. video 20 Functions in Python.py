def sum(a,b):
    sum=a+b
    print("Sum of ", a , " and ", b , " is " , sum)

def product(a,b):
    product = a*b
    print("Product of ", a , " and ", b , " is " , product)

    
def calculateGmean(a ,b):
    mean  = (a*b)/(a+b)
    print("Mean of ", a , " and ", b , " is " , mean)

    
def isgreater(a,b):
    if a>b:
        print(a ," is greater")
    elif a<b:
        print(b, "is greater")
    else:
        print(a ,"and", b , "are equal")
    
a =9
b= 8
sum(a,b)
product(a,b)
calculateGmean(a,b)
isgreater(a,b)
    
c= 8
d= 74
sum(c,d)
product(c,d)
calculateGmean(c,d)
isgreater(c,d)