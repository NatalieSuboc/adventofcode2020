def find_earliest_bus(file):
    with open(file) as txt:
        time = int(txt.readline())
        buses = [int(bus) for bus in txt.readline().split(',') if bus is not 'x']
        shortest = [0, float('inf')] # bus number, time waiting
        for bus in buses:
            time_to_wait = bus - (time % bus)
            if shortest[1] > time_to_wait:
                shortest[1] = time_to_wait
                shortest[0] = bus
    return shortest[0] * shortest[1]

from functools import reduce
import operator

def find_consecutive(file):
    with open(file) as txt:
        txt.readline() # first line is ignored
        buses = [bus for bus in txt.readline().split(',')]
        # get bus numbers and offsets
        n = [int(b) for b in buses if b != 'x']
        a = [int(b) - buses.index(b) for b in buses if b != 'x']
        return chinese_remainder(n, a)

# taken from rosettacode.org            
def chinese_remainder(n, a):
    s = 0
    prod = reduce(lambda a, b: a*b, n)
    print(prod)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        s += a_i * mul_inv(p, n_i) * p
    print(s)
    return s % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
