#Functions that use random numbers

import random
import string

def menu():
    """
    Lets the user choose what function to use
    """
    print("\nWelcome!")
    while True:
        print("\nMain Menu")
        print("Please select a function to use!")
        print("Enter 'dice' to roll a dice!")
        print("Enter 'guess' to guess a number!")
        print("Enter 'rps' to play Rock Paper Scissors!")
        print("Enter 'password' to generate a password! (A fairly weak one)")
        user_input = input(": ")

        if user_input  == "dice" or user_input == "Dice":
            dice_roll()
        elif user_input == "guess" or user_input =="Guess":
            number_guess()
        elif user_input == "rps" or user_input == "RPS":
            rock_paper_scissors()
        elif user_input == "password" or user_input =="Password":
            print("\n", password_generator(10))
        else:
            print("Invalid entry!")


def dice_roll():
    """
    Lets the user roll a dice
    Prints the result
    """
    print("Welcome!")
    while True:
        print("Press enter to roll the dice!")
        print("Enter 'quit' to exit!")
        ranDice = random.randint(1, 6)
        user_input = input(": ")
        
        if user_input == "quit" or user_input == "Quit":
            menu()
        else:
            print("The result is:", ranDice)


def number_guess():
    """
    Creates a random number
    Asks the user to guess it
    """
    print("Welcome!")
    while True:
        try:
            ranNum = random.randint(0, 10)
            print("Guess a number between 0 and 10!")
            print("Enter 'quit' to exit!")
            user_input = input(": ")
            
            if user_input == "quit":
                menu()
            else:
                user_input = float(user_input)
                if user_input == ranNum:
                    print("You guessed it!")
                elif user_input > ranNum:
                    print("Too high!")
                    print("Generating a new number...")
                elif user_input < ranNum:
                    print("Too low!")
                    print("Generating a new number...")
                elif user_input == "quit":
                    menu()
        except ValueError:
            pass
            print ("Invalid entry!")


def rock_paper_scissors():
    """
    Rock Paper Scissors Game
    """
    print("Welcome!")
    while True:
        try:
            ranRPS = random.randint(1, 3)
            if ranRPS == 1:
                ranRPS = str("Rock")
            elif ranRPS == 2:
                ranRPS = str("Paper")
            elif ranRPS == 3:
                ranRPS = str("Scissors")

            print("\nEnter 'Rock', 'Paper', or 'Scissors'!")
            print("Enter 'quit' to exit! \n")
            user_input = input(": ")
            
            if user_input == ranRPS:
                print("Computer chose:", ranRPS)
                print("Tie!")
            elif user_input == "Rock" and ranRPS == "Paper":
                print("Computer chose:", ranRPS)
                print("You Lose!")
            elif user_input == "Rock" and ranRPS == "Scissors":
                print("Computer chose:", ranRPS)
                print("You Win!")
            elif user_input == "Paper" and ranRPS == "Rock":
                print("Computer chose:", ranRPS)
                print("You Win!")
            elif user_input == "Paper" and ranRPS== "Scissors":
                print("Computer chose:", ranRPS)
                print("You Lose!")
            elif user_input == "Scissors" and ranRPS == "Rock":
                print("Computer chose:", ranRPS)
                print("You Lose!")
            elif user_input == "Scissors" and ranRPS == "Paper":
                print("Computer chose:", ranRPS)
                print("You Win!")
            elif user_input == "quit":
                menu()
            else:
                print("Invalid entry!")
        except ValueError:
            pass
            print("Invalid entry!")


def password_generator(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(stringLength))


menu()
