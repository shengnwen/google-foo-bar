__author__ = 'shengwen'
from operator import itemgetter

minions2 = [[390, 185, 624], [686, 351, 947], [276, 1023, 1024], [199, 148, 250]]
# out put [2, 3, 0, 1]
minions = [[5, 1, 5], [10, 1, 2]]
# Output:

# def answer(minions):
#     ratio_list = [(0.0 + minion[0])/((0.0 + minion[1])/minion[2])  for minion in minions]
#     return [minion[0] for minion in sorted(list(enumerate(ratio_list)), key=itemgetter(1))]


def answer(minions):
    ratio_list = [[i, (0.0 + minions[i][0])/((0.0 + minions[i][1])/minions[i][2])] for i in range(len(minions))]
    return [minion[0] for minion in sorted(ratio_list, key = lambda x: x[1])]

# ratio_list = [(0.0 + minion[0])/((0.0 + minion[1])/minion[2])  for minion in minions]
# print sorted(list(enumerate(ratio_list)), key=itemgetter(1))
print answer(minions2)

