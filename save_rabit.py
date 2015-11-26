__author__ = 'shengwen'
# Save Beta Rabbit
# ================
#
# Oh no! The mad Professor Boolean has trapped Beta Rabbit in an NxN grid of rooms. In the center of each room (except for the top left room) is a hungry zombie. In order to be freed, and to avoid being eaten, Beta Rabbit must move through this grid and feed the zombies.
#
# Beta Rabbit starts at the top left room of the grid. For each room in the grid, there is a door to the room above, below, left, and right. There is no door in cases where there is no room in that direction. However, the doors are locked in such a way that Beta Rabbit can only ever move to the room below or to the right. Once Beta Rabbit enters a room, the zombie immediately starts crawling towards him, and he must feed the zombie until it is full to ward it off. Thankfully, Beta Rabbit took a class about zombies and knows how many units of food each zombie needs be full.
#
# To be freed, Beta Rabbit needs to make his way to the bottom right room (which also has a hungry zombie) and have used most of the limited food he has. He decides to take the path through the grid such that he ends up with as little food as possible at the end.
#
# Write a function answer(food, grid) that returns the number of units of food Beta Rabbit will have at the end, given that he takes a route using up as much food as possible without him being eaten, and ends at the bottom right room. If there does not exist a route in which Beta Rabbit will not be eaten, then return -1.
#
# food is the amount of food Beta Rabbit starts with, and will be a positive integer no larger than 200.
#
# grid will be a list of N elements. Each element of grid will itself be a list of N integers each, denoting a single row of N rooms. The first element of grid will be the list denoting the top row, the second element will be the list denoting second row from the top, and so on until the last element, which is the list denoting the bottom row. In the list denoting a single row, the first element will be the amount of food the zombie in the left-most room in that row needs, the second element will be the amount the zombie in the room to its immediate right needs and so on. The top left room will always contain the integer 0, to indicate that there is no zombie there.
#
# The number of rows N will not exceed 20, and the amount of food each zombie requires will be a positive integer not exceeding 10.
# Test cases
# ==========
#
# Inputs:
food = 7
grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
# Output:
#     (int) 0
#
# Inputs:
# food = 12
# grid = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
# Output:
#     (int) 1

# def answer(food, grid):
#     N = len(grid)
#     range_grid = [[0, 0] for i in range(N * N)]
#     id = N * N - 1
#     for row in xrange(N - 1, -1, -1):
#         for col in xrange(N - 1, -1, -1):
#             if row == N - 1:
#                 if col == N - 1:
#                     range_grid[id] = [grid[row][col],grid[row][col]]
#                 else:
#                     range_grid[id] = [i + grid[row][col] for i in range_grid[id + 1]]
#             else:
#                 if col == N - 1:
#                     below = (row + 2) * (col + 1) - 1
#                     range_grid[id] = [i + grid[row][col] for i in range_grid[below]]
#                 else:
#                     below = (row + 2) * (col + 1) - 1
#                     range_grid[id][0] = grid[row][col] + min(range_grid[below][0], range_grid[id + 1][0])
#                     range_grid[id][1] = grid[row][col] + max(range_grid[below][1], range_grid[id + 1][1])
#             id -= 1
#     # print range_grid
#     if food < range_grid[0][0]:
#         return -1
#     elif food > range_grid[0][1]:
#         return food - range_grid[0][1]
#     else:
#         return 0
def answer124(food, grid):
    N = len(grid)
    range_grid = [[0, 0] for i in range(2*N)]
    for square in xrange(N - 1, -1, -1):
        if square == N - 1:
            range_grid[N - 1] = [grid[-1][-1], grid[-1][-1]]
            range_grid[2 * N - 1] = [i for i in range_grid[N - 1]]
            for id in xrange(N - 2, -1, -1):
                range_grid[id] = [range_grid[id + 1][0] + grid[N - 1][id], range_grid[id + 1][1] + grid[N - 1][id]]
                range_grid[id + N] = [range_grid[id + N + 1][0] + grid[id][N - 1], range_grid[id + N + 1][1] + grid[id][N - 1]]
            # print range_grid
        else:
            for id in xrange(square, -1, -1):
                if id == square:
                    range_grid[id][0] = grid[square][id] + min(range_grid[id][0], range_grid[id + N][0])
                    range_grid[id][1] = grid[square][id] + max(range_grid[id][1], range_grid[id + N][1])
                    range_grid[id + N] = [i for i in range_grid[id]]
                else:
                    range_grid[id][0] = grid[square][id] + min(range_grid[id][0], range_grid[id + 1][0])
                    range_grid[id][1] = grid[square][id] + max(range_grid[id][1], range_grid[id + 1][1])
                    range_grid[id + N][0] = grid[id][square] + min(range_grid[id + N][0], range_grid[id][0])
                    range_grid[id + N][1] = grid[id][square] + max(range_grid[id + N][1], range_grid[id][1])
            # print range_grid
    if food < range_grid[0][0]:
        return -1
    elif food > range_grid[0][1]:
        return food - range_grid[0][1]
    else:
        return 0

        # for id in xrange(N - 1, - 1, - 1):
        #     if id == square:
        #     # row
        #     # col
        #     range_grid[N - 1] = [grid[-1][0], grid[-1][0]]
        #     range_grid[2 * N - 1] = [i for i in range_grid[N - 1]]


def answer(food, grid):
    N = len(grid)
    range_grid = [[0, 0] for i in range(2*N)]
    for square in xrange(N - 1, -1, -1):
        if square == N - 1:
            range_grid[N - 1] = [grid[-1][-1], grid[-1][-1]]
            range_grid[2 * N - 1] = [i for i in range_grid[N - 1]]
            for id in xrange(N - 2, -1, -1):
                range_grid[id] = [range_grid[id + 1][0] + grid[N - 1][id], range_grid[id + 1][1] + grid[N - 1][id]]
                range_grid[id + N] = [range_grid[id + N + 1][0] + grid[id][N - 1], range_grid[id + N + 1][1] + grid[id][N - 1]]
            # print range_grid
        else:
            for id in xrange(square, -1, -1):
                if id == square:
                    range_grid[id][0] = grid[square][id] + min(range_grid[id][0], range_grid[id + N][0])
                    range_grid[id][1] = grid[square][id] + max(range_grid[id][1], range_grid[id + N][1])
                    range_grid[id + N] = [i for i in range_grid[id]]
                else:
                    range_grid[id][0] = grid[square][id] + min(range_grid[id][0], range_grid[id + 1][0])
                    range_grid[id][1] = grid[square][id] + max(range_grid[id][1], range_grid[id + 1][1])
                    range_grid[id + N][0] = grid[id][square] + min(range_grid[id + N][0], range_grid[id][0])
                    range_grid[id + N][1] = grid[id][square] + max(range_grid[id + N][1], range_grid[id][1])
            print range_grid
    if food < range_grid[0][0]:
        return -1
    elif food > range_grid[0][1]:
        return food - range_grid[0][1]
    else:
        return 0

print answer(food,grid)

