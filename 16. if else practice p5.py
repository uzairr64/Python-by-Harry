age1 = int(input("Enter First Person's Age: "))
age2 = int(input("Enter Second Person's Age: "))
age3 = int(input("Enter Third Person's Age: "))

print("Age of First Person: " , age1)
print("Age of Second Person: " , age2)
print("Age of Third Person: " , age3)

if age1 > age2 and age1 > age3:
    print("/nFirst Person is elder!")
    
elif age2 > age1 and age2 > age3:
    print("Second Person is elder!")
    
elif age3 > age1 and age3 > age2:
    print("Third Person is elder!")
    
else:
    print("All Persons are Equal in Age!")