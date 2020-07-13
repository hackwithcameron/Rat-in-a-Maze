from maze import print_maze, create_blank, get_maze_size,\
    maze_1, maze_2, maze_3, maze_4


def rat(maze):
    start_pos = (0, 0)
    solution = create_blank(maze)
    maze_height, maze_width = get_maze_size(maze)
    print(f"Input Maze Height: {maze_height} Width: {maze_width}")
    print_maze(maze)  # Prints maze

    if not find_path(maze, start_pos, solution, maze_width, maze_height):
        return print("No solution!")
    print("Solution")
    print_maze(solution)


def finish(pos, maze, maze_width, maze_height):
    x, y = pos
    if is_valid(maze, pos, maze_width, maze_height) is True:
        location = maze[x][y]
        if location == 2:
            return True


def find_path(maze, pos, solution, maze_width, maze_height):
    x, y = pos  # Unpacks coordinates
    if finish(pos, maze, maze_width, maze_height):
        solution[x][y] = 1
        return True
    if is_valid(maze, pos, maze_width, maze_height) is True:
        solution[x][y] = 1
        if find_path(maze, (x + 1, y), solution, maze_width, maze_height) is True:
            return True
        if find_path(maze, (x, y + 1), solution, maze_width, maze_height) is True:
            return True
        solution[x][y] = 0
        return False


def is_valid(maze, pos, maze_width, maze_height):
    x, y = pos
    if 0 <= x < maze_height and 0 <= y < maze_width and maze[x][y]:
        return True
    return False


if __name__ == "__main__":
    rat(maze_4)
