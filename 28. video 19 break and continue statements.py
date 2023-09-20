n = 5
for i in range(1,11):
    if i == 6:
        break
    m = n * i
    print(n , "*" , i , "=" , m)
    
print("Next!")
for i in range(1,11):
    if i == 6:
        continue
    m = n * i
    print(n , "*" , i , "=" , m)