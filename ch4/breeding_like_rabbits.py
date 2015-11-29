__author__ = 'shengwen'


r = {0:1, 1:1, 2:2}

def R(n):
    global r
    if n in r:
        return r[n]
    if n % 2 == 0:
        mid_n = n / 2
        r[n] = R(mid_n) + R(mid_n + 1) + mid_n
    else:
        mid_n = n / 2
        r[n] = R(mid_n - 1) + R(mid_n) + 1
    return r[n]

def binary_search(f, zombits):
    start, end = 0, zombits
    while start <= end:
        mid = (start + end) / 2
        mid_f_val = R(f(mid))
        # print "mid:" + str(f(mid)) + ", val:" + str(mid_f_val)
        if mid_f_val == zombits:
            return mid
        elif mid_f_val < zombits:
            start = mid + 1
        else:
            end = mid - 1
    return -2


def answer(zombits):
    ans = []
    zombits = int(zombits)
    even_ans = binary_search(lambda x: x * 2, zombits) * 2
    odd_ans = binary_search(lambda x: x * 2 + 1, zombits) * 2 + 1
    if even_ans >= 0:
        # print even_ans
        ans.append(even_ans)
    if odd_ans >= 0:
        # print odd_ans
        ans.append(odd_ans)
    if len(ans) == 0:
        return "None"
    else:
        return str(max(ans))

print answer(str(100))
