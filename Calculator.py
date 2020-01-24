#Simple Calculator program
def the_calc():
    """
    Calculates based off of user input
    This is an example of a docstring
    """
    print("Welcome!")
    while True:
        try:
                
            print("\nOptions Menu")
            print("Enter 'add' to add two numbers")
            print("Enter 'subtract' to subtract two numbers")
            print("Enter 'multiply' to multiply two numbers")
            print("Enter 'divide' to divide two numbers")
            print("Enter 'quit' to exit the program")
            user_input = input(": ")
            
            if user_input == "quit":
                               break
            elif user_input == "add":
                               add1 = float(input("Type the first number:"))
                               add2 = float(input("Type the second number:"))
                               add3 = float(add1) + float(add2)
                               print ("The result is:", add3)
                               contconfirm = input("Press enter to continue:")
            elif user_input == "subtract":
                               subtract1 = float(input("Type the first number:"))
                               subtract2 = float(input("Type the second number:"))
                               subtract3 = float(subtract1) - float(subtract2)
                               print ("The result is:", subtract3)
                               contconfirm = input("Press enter to continue:")
            elif user_input == "multiply":
                               multiply1 = float(input("Type the first number:"))
                               multiply2 = float(input("Type the second number:"))
                               multiply3 = float(multiply1) * float(multiply2)
                               print ("The result is:", multiply3)
                               contconfirm = input("Press enter to continue:")
            elif user_input == "divide":
                               divide1 = float(input("Type the first number:"))
                               divide2 = float(input("Type the second number:"))
                               divide3 = float(divide1) / float(divide2)
                               print ("The result is:", divide3)
                               contconfirm = input("Press enter to continue:")
            else:
                               print("Unknown Input")
        except ValueError:
            pass
            print("Invalid entry!")

the_calc()

