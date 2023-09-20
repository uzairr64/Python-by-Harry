#Python program to print a multiplication table of a given number

num = int(input("Enter a number: "))

print("Table of",num,"is: ")
for i in range(1,11):
    m = num*i
    print(num,"*",i,"=",m)
    