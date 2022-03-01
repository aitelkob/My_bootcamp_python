import sys


def parsing_check(argv):
    usage = "Usage: python operations.py <number1> <number2>\nExample:\n"
    usage_2 = "python operations.py 10 3"
    usage = usage + usage_2
    if (len(argv) == 0):
        print(usage)
        exit()
    elif (len(argv) != 2):
        print("InputError: too many arguments\n\n" + usage)
        exit()
    elif not argv[0].isdigit() or not argv[1].isdigit():
        print("InputError: only numbers\n\n" + usage)
        exit()
    return argv


def print_format(argv):
    number = [int(i) for i in argv]
    print("Sum:        {}".format(number[0] + number[1]))
    print("Difference: {}".format(number[0] - number[1]))
    print("Product:    {}".format(number[0] * number[1]))
    if (number[0] > 0 and number[1] > 0):
        print("Qutient:    {}".format(number[0] / number[1]))
        print("Remainder:  {}".format(number[0] % number[1]))
    else:
        print("Qutient:    ERROR (div by zero)")
        print("Remainder:  ERROR (modulo by zero)")


argv = parsing_check(sys.argv[1:])
print_format(argv)
