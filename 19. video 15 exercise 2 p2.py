import time
time = time.strftime("%H: %M: %S")
print(time)

if time >= "24: 00: 00" and time < "12: 00: 00":
    print("It is Morning!")
    
elif time >= "12: 00: 00" and time < "16: 00: 00":
    print("It is Afternoon!")
    
else:
    print("It is Evening")


