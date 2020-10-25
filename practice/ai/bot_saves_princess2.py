# https://www.hackerrank.com/challenges/saveprincess2/problem

def nextMove(n,r,c,grid):
    bot_position = (r, c)
    princess_position = (None, None)

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "p":
                princess_position = (i, j)

    y = abs(bot_position[0] - princess_position[0])
    if y > 0:
        return "DOWN" if bot_position[0] < princess_position[0] else "UP"
    x = abs(bot_position[1] - princess_position[1])
    if x > 0:
        return "RIGHT" if bot_position[1] < princess_position[1] else "LEFT"