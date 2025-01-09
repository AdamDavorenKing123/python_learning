# typecasting = the process of converting a variable from one data type to another
#                str(), int(), float(), bool()

#name = "Adam"
#age = 19
#gpa = 3.2
#is_student = True
#print(type(is_student))

#age = str(age)
#print(age)
#print(type(age)) number is now a string

#name = bool(name)
#print(name)   If string variable contain char True
              #else false
              #could be used to see if user has input something

##########################################
#input()  = A function that prompt the user to enter data
# returns the entered data as a string

# name = input("What is your name?: ")
# age = int(input("How old are you?; ")) # type casting string to int
# #age = int(age) # removes the need for doing this
# age = age + 1
#
# print(f"Hello {name}!")
# print("Happy Birthday")
# print(f"You are {age} years old")

###################################################################
# Exercise 1 Rectangle Area Calc

# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))
# area = length * width
#
# print(f"The area is: {area}cm^2")

# Exercise 2 Shopping Cart Program

# item = input("What item would you like to buy?: ")
# price = float(input("What is the price?"))
# quantity =  int(input("How many would you like?"))
# total = price*quantity
#
# print(f"You have bought {quantity} x {item}/s")
# print(f"Your total is: €{total}")