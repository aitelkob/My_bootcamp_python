import sys

if (len(sys.argv) == 3):
    if not (sys.argv[-1].isdigit()):
        print("ERROR")
        exit()
else:
    print("Too few or many arguments.")
    exit()

string = sys.argv[1]
n = int(sys.argv[2])

string_out = ' '.join([w for w in string.split() if (len(w) > n)])
list_string = list(string_out.split(' '))
print(list_string)
