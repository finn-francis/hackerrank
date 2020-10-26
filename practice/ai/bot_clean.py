# https://www.hackerrank.com/challenges/botclean?hr_b=1

# 1 - Find the positions of each dirty cell
# 2 - Find the cell with fewest jumps
# 3 - Direct towards the closes cell

def next_move(bot_row, bot_col, grid):
    shortest_jump = {"row": float("inf"), "col": float("inf"), "hops": float("inf")}

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "d":
                if (i == bot_row and j == bot_col):
                    return "CLEAN"
                hops = abs(bot_row - i) + abs(bot_col - j)
                if shortest_jump["hops"] > hops:
                    shortest_jump = {"row": i, "col": j, "hops": hops}

    if abs(shortest_jump["row"] - bot_row) > abs(shortest_jump["col"] - bot_col):
        return "DOWN" if shortest_jump["row"] > bot_row else "UP"
    else:
        return "LEFT" if shortest_jump["col"] < bot_col else "RIGHT"
