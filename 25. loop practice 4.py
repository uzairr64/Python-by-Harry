#Python program to calculate the sum of all the odd numbers within the given range.

s = int(input("enter your starting number: "))
e = int(input("enter your ending number: "))

sum = 0
for i in range(s,e):
    if i%2 != 0:
        sum = sum+i 
print("sum of all odd numbers: " , sum)