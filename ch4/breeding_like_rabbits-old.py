__author__ = 'shengwen'

r = {0: 1, 1: 1, 2: 2}
def R(count):
    """Work backwards to compute R(n)."""
    if count not in r:
        n = count // 2
        if count == 2 * n:
            r[count] = R(n) + R(n + 1) + n
        else:
            r[count] = R(n - 1) + R(n) + 1
    return r[count]


def binary_search(space, zombits):
    start, end = 0, zombits
    while start <= end:
        mid = (start + end) // 2
        probe = R(space(mid))
        if probe == zombits:
            return mid
        if probe < zombits:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def answer(zombits):
    zombits = int(zombits)
    bs_even = binary_search(lambda n: n * 2, zombits) * 2
    bs_odd = binary_search(lambda n: n * 2 + 1, zombits) * 2 + 1
    if bs_even < 0:
        answer = None if bs_odd < 0 else bs_odd
    elif bs_odd < 0:
        answer = bs_even
    else:
        answer = max(bs_even, bs_odd)
    return '{}'.format(answer)


print answer(str(10**20))
