__author__ = 'shengwen'

def answer(t, n):
    current = [0] * n
    current[-1] = 1

    last = [0] * n
    for step in xrange(t):
        current