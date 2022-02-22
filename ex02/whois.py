import sys

if len(sys.argv) == 1:
    print(" ")
else: 
    argv = sys.argv[1:]
    if (argv[0].isdigit() != True):
        print("AssertionError: argument is not integer")
    elif (len(argv) != 1):
        print("AssertionError: more than one argument is provided")
    else:
        number = int(argv[0])
        if number == 0:
            print("I’m Zero.")
        elif (number % 2) == 0:
            print("I’m Even.")
        else:
            print("I’m Odd.")  
