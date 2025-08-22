
import random

def get_user_input():
    while True:
        try:
            return int(input("Enter a number between 1 and 100: "))
        except ValueError:
            print("Invalid input. Please enter a number.")

def guess_the_number():
    # take in a number  we will have a predefined guess
        
    print("you have 10 chances")
    user = int(input("enter a number between 1, 100"))
    guess =random.randint(1,100)
    for i in range(10):
        if user==guess :
            print("you guessed right")
        
        elif user>guess:
            print("your guess is higher")
            user =int(input('try again enter another number '))
        
        elif user<guess:
            print("your guess is lower")
            user =int(input('try again enter another number'))
        
        else:
          print("our number is out of scope")
    else:
        print("you runned out of chances")

guess_the_number()
