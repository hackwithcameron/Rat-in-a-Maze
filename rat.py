from maze import print_maze, create_blank, maze_1, maze_2


def rat(maze):
    start_pos = (0, 0)
    solution = create_blank(maze)
    print("Input Maze")
    print_maze(maze)  # Prints maze

    if not find_path(maze, start_pos, solution):
        return print("No solution!")
    print("Solution")
    print_maze(solution)


def finish(pos, maze):
    x, y = pos
    if is_valid(maze, pos) is True:
        location = maze[x][y]
        if location == 2:
            return True


def find_path(maze, pos, solution):
    x, y = pos  # Unpacks coordinates
    if finish(pos, maze):
        solution[x][y] = 1
        return True
    if is_valid(maze, pos) is True:
        solution[x][y] = 1
        if find_path(maze, (x + 1, y), solution) is True:
            return True
        if find_path(maze, (x, y + 1), solution) is True:
            return True
        solution[x][y] = 0
        return False


def is_valid(maze, pos):
    x, y = pos
    if 0 <= x < 5 and 0 <= y < 5 and maze[x][y]:
        return True
    return False


if __name__ == "__main__":
    rat(maze_1)
    rat(maze_2)
