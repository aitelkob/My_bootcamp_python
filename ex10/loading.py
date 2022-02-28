import datetime
import time


def ft_progress_testing(lst):
    start = datetime.datetime.now()
    end = len(lst) * 0.05
    index = 0
    long = len(lst)
    for step in lst:
        index += 1
        nowtime = datetime.datetime.now() - start
        secon = nowtime.microseconds/1000000 + nowtime.seconds
        if step == lst[0]:
            eta = 0
            etap = 0
        elif step == lst[1]:
            eta = secon * len(lst)
            etap = secon
            eta = eta - etap
        else:
            eta = eta - etap
        percen = int(index/len(lst) * 100)
        icon = int(percen / 5)
        print("\033c", end="")
        print("ETA: {} [{}%]".format(((str(round(abs(eta - etap), 2)) +
              "s").ljust(6, ' ')), percen), end="")
        print("[" + "=" * icon + ">" + " " * (20 - icon) + "]", end=" ")
        print("{}/{}".format((str(index)), (str(long))), end="")
        print(" | elapsed time  {}".format(str(round(secon, 2)) + "s"))
        print("...")
        yield step


listy = range(3000)
ret = 0
for elem in ft_progress_testing(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)
