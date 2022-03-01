import sys


if len(sys.argv) == 1:
    exit()
else:
    argv = sys.argv[1:]
    if not (argv[0].isdigit()):
        print("AssertionError: argument is not integer")
        print("")
    elif (len(argv) != 1):
        print("AssertionError: more than one argument is provided")
        print("")
    else:
        number = int(argv[0])
        if number == 0:
            print("I’m Zero.")
            print("")
        elif (number % 2) == 0:
            print("I’m Even.")
            print("")
        else:
            print("I’m Odd.")
            print("")
