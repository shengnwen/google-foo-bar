__author__ = 'shengwen'

# steps = ['Left', 'Stay', 'Right']
# dp[i] represent all sequence in dp[i]
def answer(t, n):
    # your code here
    if n > t + 1:
        return 0
    if n == 2:
        return t
    if t == n:
        return n
    lst = [0] * n
    lst2 = [0] * n
    total = 0
    lst[0] = 1
    lst[1] = 1
    max = 1
    for i in xrange(1, t):
        lst2 = [0] * n
        if max < n - 1:
            max += 1
        for j in xrange(0, n):
            if j >= (max + 1):
                break
            if j == 0:
                lst2[j] = lst[j] + lst[j + 1]
            elif j == max:
                if j == n - 1:
                    total += lst[j - 1]
                else:
                    lst2[j] = lst[j - 1]
            else:
                lst2[j] = lst[j - 1] + lst[j] + lst[j + 1]
        lst = lst2
    return total % 123454321

# print answer(3, 1)

