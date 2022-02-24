import sys
import random


print("This is an interactive guessing game!")
print("You have to find a secret number between 1 and 99.")
print("Type 'exit' to end the game.")
print("Good luck!")
num = random.randint(1, 99)
cpt_try = 1

while 1:
    choie = input("What's your guess between 1 and 99?\n>> ")
    if choie == 'exit':
        print("Bye!")
        break
    else:
        if (not type(1) == int(choie)):
            print("That's not a number.")
            cpt_try+=1
            if choie < 1 or choie > 99:
            print("Number is out of range.")
    elif choie < num:
        print("Too low!")
    elif choie > num:
        print("Too high!")
    elif choie == num and cpt_try == 1:
        print("Congratulations, you got it first try!!!")
        break
    elif choie == num and cpt_try > 1:
        print("You got it!")
        print("You won in {} cpt_trys!".format(cpt_try))
        break
    cpt_try += 1

