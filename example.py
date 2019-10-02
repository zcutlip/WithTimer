from time import sleep
from withtimer.withtimer import Timer


def func1(count):
    for i in range(0, 3):
        with Timer("Calling func2"):
            func2(2)
    print("func1 sleeping {}".format(count))
    sleep(count)


def func2(count):
    print("func2 sleeping {}".format(count))
    sleep(count)


if __name__ == "__main__":
    Timer.enable_timing(True)
    with Timer("main"):
        for i in range(0, 3):
            if i % 2 > 0:
                func1(i + 1)
