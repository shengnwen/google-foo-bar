__author__ = 'shengwen'

meetings = [[0, 1], [1, 2], [2, 3], [3, 5], [4, 5]]
# meetings = [[0, 1000000], [42, 43], [0, 1000000], [42, 43]]
# def answer(meetings):
#     if len(meetings) == 0:
#         return 0
#     sorted_meetings = sorted(meetings, key=lambda x: (x[0], x[1]))
#     prev = None
#     result = []
#     for i in sorted_meetings:
#         if i[0] >= i[1]:
#             continue
#         if prev is None or i[0] >= prev[1]:
#             prev = [i[0], i[1]]
#             result.append(prev)
#         elif i[1] > prev[1]:
#             prev[1] = i[1]
#     return len(result)
#
# def answer(meetings):
#     if len(meetings) == 0:
#         return 0
#     sorted_meetings = sorted(meetings, key=lambda x: x[0])
#     result = []
#     for i in sorted_meetings:
#         overlap = False
#         for sample in result:
#             if i[0] < sample[1] and i[1] > sample[0]:
#                 overlap = True
#                 break
#         if not overlap:
#             result.append(i)
#     return len(result)

def answer(meetings):
    if len(meetings) == 0:
        return 0
    sorted_meetings = sorted(meetings, key=lambda x: (x[0], x[1]))
    result = []
    for i in sorted_meetings:
        overlap = False
        if i[0] >= i[1]:
            continue
        for sample in result:
            if i[0] < sample[1] and i[1] > sample[0]:
                overlap = True
                break
        if not overlap:
            result.append(i)
    return len(result)

print answer(meetings)


