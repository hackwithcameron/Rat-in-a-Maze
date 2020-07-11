from maze import print_maze, maze_1


def rat(maze, pos):
    print_maze(maze)
    if finish(maze, pos):
        return True
    else:
        new_position = find_next(maze, pos)
        if new_position not in pos:
            rat(maze, new_position)


def finish(maze, pos):
    location = maze[pos[0]][pos[1]]
    if location == 2:
        return True
    else:
        return False


def find_next(maze, pos):
    location = maze[pos[0]][pos[1]]
    down = maze[pos[0] + 1][pos[1]]
    right = maze[pos[0]][pos[1] + 1]
    up = maze[pos[0] - 1][pos[1]]
    left = maze[pos[0]][pos[1] - 1]
    if up == 1:
        return pos[0] + 1, pos[1]
    if right == 1:
        return right
    if down == 1:
        return down
    if left == 1:
        return left
    else:
        return location




if __name__ == "__main__":
    start_pos = (0, 0)
    rat(maze_1, start_pos)
