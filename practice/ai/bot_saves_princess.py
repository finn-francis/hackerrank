# https://www.hackerrank.com/challenges/saveprincess?hr_b=1

def save_princess(grid):
    bot_position = (None, None)
    princess_position = (None, None)

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "m":
                bot_position = (i, j)
            elif cell == "p":
                princess_position = (i, j)

    y = abs(bot_position[0] - princess_position[0])
    x = abs(bot_position[1] - princess_position[1])
    y_direction = "DOWN" if bot_position[0] < princess_position[0] else "UP"
    x_direction = "RIGHT" if bot_position[1] < princess_position[1] else "LEFT"

    return "\n".join([x_direction] * x + [y_direction] * y)