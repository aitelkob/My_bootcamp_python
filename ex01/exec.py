import sys

def reverse(x):
    return x[::-1]
if len(sys.argv) == 1:
    print(" ")
else:
    argv = sys.argv[1:]
    str = reverse(' '.join(argv))
    print(str.swapcase())
