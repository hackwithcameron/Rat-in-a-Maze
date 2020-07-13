from maze import print_maze, create_blank, \
    test, example


def rat(maze):
    """
    Main function called to find path through maze.

    :param maze: Maze for path to be found
    :return: Solution to maze or "No solution"
    """
    start_pos = (0, 0)
    solution = create_blank(maze)  # Creates blank maze same size of original
    print(f"Input Maze \nHeight:{len(maze)} Width:{len(maze[0])}")
    print_maze(maze)  # Prints input maze

    if not find_path(maze, start_pos, solution):
        return print("No solution!")
    print("Solution")
    return print_maze(solution)


def finish(pos, maze):
    """
    Checks if position is a valid spot before checking for finish
    :param pos: Position of Rat
    :param maze: Input maze
    :return: True if position id valid and location is not finish.
    """
    x, y = pos
    if is_valid(maze, pos) is True:  # Make sure position is valid before checking for finish
        location = maze[x][y]
        if location == 2:  # If location is finish return True
            return True


def find_path(maze, pos, solution):
    """
    Recursive function the finds path from start position to finish if possible.

    :param maze: Input maze
    :param pos: Position of Rat (start position = (0, 0))
    :param solution: Solution for input maze
    :return: Solution for maze or False
    """
    x, y = pos  # Unpacks coordinates
    if finish(pos, maze):  # Checks to see if rat is at finish
        solution[x][y] = 1  # Sets position to 1 on solution showing complete path
        return True
    if is_valid(maze, pos) is True and solution[x][y] != 1:  # Checks to see if position is valid and position is not
        solution[x][y] = 1                                   # already in solution
        if find_path(maze, (x + 1, y), solution) is True:
            return True
        if find_path(maze, (x, y + 1), solution) is True:
            return True
        if find_path(maze, (x - 1, y), solution) is True:
            return True
        if find_path(maze, (x, y - 1), solution) is True:
            return True
        solution[x][y] = 0
        return False


def is_valid(maze, pos):
    x, y = pos
    if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y]:
        return True
    return False


if __name__ == "__main__":
    rat(example)
