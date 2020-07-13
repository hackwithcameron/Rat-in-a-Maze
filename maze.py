# 0 = wall, 1 = path/start in top left, 2 = end.
maze_1 = [
    [1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 2]
]

maze_2 = [
    [1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 2],
]

maze_3 = [
    [1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 2]
]

maze_4 = [
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 2, 1, 0, 1, 0, 1, 1, 1, 2]
]


def print_maze(maze):
    for row in maze:
        print(row)
    print("- - - - - - - - -")


def create_blank(maze):
    blank_maze = [[0 for j in range(len(maze[0]))] for i in range(len(maze))]
    return blank_maze


def get_maze_size(maze):
    x = 0
    y = 0
    for i in maze:
        x += 1
        for j in i:
            y += 1
    y //= x
    return x, y
