
# 0 = wall, 1 = path/start in top left, 2 = end.
maze_1 = [
    [1, 0, 0, 0, 0],
    [1, 1, 1, 0, 2],
    [0, 1, 0, 1, 1],
    [1, 1, 1, 1, 0]
]

def print_maze(maze):
    for row in maze:
        print(row)
    print(" - - - - - - - - - ")
