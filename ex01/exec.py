import sys

def reverse(x):
    x.swapcase()
    print(x)
    return x[::-1]

argv = sys.argv[1:]
str = reverse(' '.join(argv[::-1]))
test = str.
print(str)
