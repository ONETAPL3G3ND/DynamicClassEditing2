import sys

class Test:
    def __init__(self):
        local = sys._getframe(1).f_locals
        self.__dict__.update(
            (key, value) for key, value in local.items()
        if callable(value))


def TestDef():
    print("TestDef")

def TestData():
    print("TestData")

if __name__ == '__main__':
    t = Test()
    t.TestData()
    t.TestDef()