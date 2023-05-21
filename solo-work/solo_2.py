# import
from math import pi


def romb(h, a):
    obwod = 4 * a
    pole = a * h
    return obwod, pole

print(f"Obwod i pole rombu wynosi {romb(10, 4)}")


def kolo(r):
    obwod = 2 * pi * r
    pole = pi * r ** 2
    return obwod, pole

print(f"Obwod i pole koła wynosi {kolo(10)}")
