# take in a number  we will have a predefined guess
#
import random
print("you have 10 chances")
user = int(input("enter a number between 1, 100"))
guess =random.randint(1,100)
for i in range(10):
  if user==guess :
    print("you guessed right")
    break
  elif user>guess:
    print("your guess is higher")
    user =int(input('try again enter another number '))
    continue
  elif user<guess:
    print("your guess is lower")
    user =int(input('try again enter another number'))
    continue
  else:
    print("our number is out of scope")
else:
  print("you runned out of chances")