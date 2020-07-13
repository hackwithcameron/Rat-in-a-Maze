# Rat-in-a-Maze

##### Solves nxn Maze. 

## Covers:
* Backtracking algorithm
* Displaying data
* Recursion
* Nested loops
* List comprehension

<hr>

## Overview:
  This is a solution to the Rat-in-a-maze problem using a recursive funtion and the backtracking algorithm. The program takes in an input maze that can be any rectangular dimensions example: 4x4, 7x9, or 15x12. This does not find the shortest path. Most other solutions only include movement to be right or down, I included the ability to move in all directs to solve more complicated mazes. 

<hr>

## Example:
![Rat-in-a-maze Example](https://github.com/hackwithcameron/Rat-in-a-Maze/blob/master/images/Rat-in-a-maze_example.png)

<hr>

## Problems:
I was getting part of the solution, but everytime I reach a dead end my printed solution would stop at that point and return the wrong solution.

![Problem solution](https://github.com/hackwithcameron/Rat-in-a-Maze/blob/master/images/problem_solution.png)

<hr>

## Solution:
  I figured out that I needed to call my is_valid() function before I check the location for the finish
  
```
def finish(pos, maze):
  x, y = pos
    if is_valid(maze, pos) is True:  # Make sure position is valid before checking for finish
        location = maze[x][y]
        if location == 2:  # If location is finish return True
            return True
            
def is_valid(maze, pos):
    x, y = pos
    if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y]:
        return True
    return False
```

![Solution](https://github.com/hackwithcameron/Rat-in-a-Maze/blob/master/images/right_solution.png)
<hr>
