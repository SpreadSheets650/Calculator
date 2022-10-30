
# Author : Soham Maity
# Class : IX Science A
# www.spreadsheets650.tech

# Program make a simple calculator

# operation functions

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# UI - printing statements

print("Select An Operation To Perform :")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# logic functions

while True:
    # take input from the user
    choice = input("Enter Your Choice In ( 1 / 2 / 3 / 4 ) : ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Should We Do Another Calculation ? ( Yes / No ) : ")
        if next_calculation == "no":
            print ("Thank You For Using My Calculator | Please Rate It Between 0 - 10")
            rate = int(input("Your Rating : "))
            
        if rate <= 5:
            print ("It is Sad To hear That Will Try to Fix It And Improve It Next Time")
        if rate > 5:
            print ("Thank You For Your Amazing Rate")
        if rate >= 10:
            print ("WoW Your Rating Is Beyond Imagination | Thank You")
        
        
            break
     
    
    else:
        print("Invalid Input")
