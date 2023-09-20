#A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#Take following input from user
#Number of classes held
#Number of classes attended.
#And print
#percentage of class attended
#Is student is allowed to sit in exam or not.

classes = int(input("Total No. of Classes Held: "))
attend = int(input("Total No. of Attended Classes: "))

percentage = (attend/classes)*100
print("Student Attendence Percentage is: " , percentage , "%")

if percentage < 75:
    medical_cause =input("Kindly Inform us that you have medical issue or not: ")
    if medical_cause is "Yes":
        print("Student Allowed to Sit in Exam!")
    else:
        print("Student not Allowed to Sit in Exam!")
        
else:
    print("Student Allowed to Sit in Exam!")

