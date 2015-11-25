__author__ = 'shengwen'

import math
def answer(x):
    length = math.ceil(math.log(x * 2 + 1, 3))
    sign = ['L', '-', 'R']
    result = []
    while x != 1:
        delta = int(x - (3 ** (length - 1) - 1)/2 - 1)
        val = delta % 3
        result.append(sign[val])
        length -= 1
        x = math.floor(delta / 3) + (3 ** (length - 1) - 1)/2 + 1
    result.append('R')
    return result

for i in range(1, 15):
    print answer(i)