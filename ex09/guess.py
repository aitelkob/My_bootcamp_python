import sys
import random


print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")
num = random.randint(1, 99)
cpt_try = 1

while 1:
    choie = input("What's your guess between 1 and 99?\n>> ")
    if choie == 'exit':
        print("Bye!")
        break
    elif (not choie.isdigit()):
        print("That's not a number.")
        cpt_try +=1
    else:
        cpt_try += 1
        choie = int(choie)
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
            print("Congratulations, you've got it!")
            print("You won in {}  attempts!".format(cpt_try))
            break
            cpt_try += 1
        else:
            print("Work")
