budget = int(input("enter your Budget: "))
print("Your Budget is: " , budget)
apple_price = 150

if(apple_price < budget ):
    print("Add 1kg Apple to Cart")

elif(apple_price > budget):
    print("Alexa! Don't Add Apple to Cart")
    
else:
    print("Alexa! Don't need Apples Today")