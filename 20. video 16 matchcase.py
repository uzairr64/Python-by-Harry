variable = int(input("enter a number: "))

match variable:
    case 0:
        print("Variable is: " , variable)
    
    case 1:
        print("Variable is; " , variable)
        
    case _:
        print("Variable is Default")
