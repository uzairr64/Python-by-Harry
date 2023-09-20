#Python program to print all the even numbers within the given range.
s = int(input("enter your starting point: "))
e = int(input("enter your ending point: "))

print("Even Numbers are: ")
for i in range(s,e):
    if i % 2 == 0:
        print(i)