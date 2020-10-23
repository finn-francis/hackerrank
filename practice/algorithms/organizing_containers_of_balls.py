# https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem

# David wants to perform some number of swap operations such that:
# - Each container contains only balls of the same type.
# - No two balls of the same type are located in different containers.

# 1 - Find the capacity of each container
# 2 - Find how many of each ball type there is
# 3 - Check that there is a configuration of balls that will work

def organize_containers(container, n):
    containers = [0] * n
    ball_types = [0] * n

    for i, row in enumerate(container):
        for j, cell in enumerate(row):
            containers[i] += cell
            ball_types[j] += cell

    return "Possible" if sorted(containers) == sorted(ball_types) else "Impossible"