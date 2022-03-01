import sys


def testing():
    lis = []
    if len(sys.argv) < 2:
        return
    list = sys.argv[:0:-1]
    for word in list:
        if not (len(word) == 0):
            lis.append(word[::-1])
    if len(lis) != 0:
        print(' '.join(lis).swapcase())


testing()
