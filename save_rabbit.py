__author__ = 'shengwen'

food = 12
grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]

def answer(food, grid):
    N = len(grid)
    ans_grid = [[set() for i in range(N)] for j in range(2*N)]
    ans_grid[0][0] |= {grid[0][0]}
    for (row, row_val) in enumerate(grid):
        for (col, val) in enumerate(row_val):
            if row != 0:
                ans_grid[row][col] |= {val + x for x in ans_grid[row - 1][col] if (val + x) <= food}
            if col != 0:
                ans_grid[row][col] |= {val + x for x in ans_grid[row][col - 1] if (val + x) <= food}
    answers = sorted(ans_grid[N - 1][N - 1], reverse= True)
    if len(answers) == 0 or answers[-1] > food:
        return -1
    for food_used in answers:
        if food_used <= food:
            return food - food_used



# def answer(food, grid):
#     N = len(grid)
#     ans_grid = [[set() for i in range(N)] for j in range(N)]
#     ans_grid[0][0] |= {grid[0][0]}
#     for (row, row_val) in enumerate(grid):
#         for (col, val) in enumerate(row_val):
#             if row != 0:
#                 ans_grid[row][col] |= {val + x for x in ans_grid[row-1][col]
#                                        if (val + x) <= food}
#             if col != 0:
#                 ans_grid[row][col] |= {val + x for x in ans_grid[row][col-1]
#                                        if (val + x) <= food}
#     all_ans = sorted(ans_grid[N-1][N-1], reverse=True)
#     print "all_ansewr" + str(all_ans)
#     for el in all_ans:
#         if el <= food:
#             return food-el
#     return -1
print answer(food, grid)
N = len(grid)
ans_grid = [[set() for i in range(N)] for j in range(N)]
print ans_grid
ans_grid[0][0] |= {grid[0][0]}
print(ans_grid[0][0])
