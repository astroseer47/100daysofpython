def add(*args):
    total = 0
    for arg in args:
        total = total + arg
    print(total)

def calculate(**kwargs):
    n = 0
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

add(1,2,3,41)

calculate(add=3, multiply=5)


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)