"""
maze generator

Uses the recursive division method to generate a maze. The algorithm is as follows: start with a rectangle of blank
cells. Pick a random location along the width and draw a line across the rectangle, do the same for the height.
There are now four walls. Select three of them at random, and create one gap in each in a random position.
Recursively apply this process to each of the 4 resultant rectangles, util each rectangle is length 1 in at least one
direction.
"""

# this is officially the most ridiculous code I have ever written

import numpy as np

# width, height
DIMENSION = [12, 10]


def generate_maze(empty_grid, dimension):
    print "dimensions: ", dimension
    # base case
    if dimension[0] <= 2 or dimension[1] <= 2:
        print "got here"
        return empty_grid
    else:
        # low is inclusive, high is exclusive
        width_split = np.random.randint(1, dimension[0] - 1)
        height_split = np.random.randint(1, dimension[1] - 1)
        print "width split: ", width_split
        print "height split: ", height_split

        vertical_wall = [row[width_split] for row in empty_grid]
        horizontal_wall = empty_grid[height_split]

        # change to 1s
        vertical_wall = [1 for _ in vertical_wall]
        horizontal_wall = [1 for _ in horizontal_wall]

        # divide into 4 separate walls
        north_wall = [vertical_wall[i] for i in range(height_split)]
        south_wall = [vertical_wall[i] for i in range(height_split, dimension[1])]
        east_wall = [horizontal_wall[i] for i in range(width_split)]
        west_wall = [horizontal_wall[i] for i in range(width_split, dimension[0])]

        # select three random walls to have gaps
        walls = [north_wall, south_wall, east_wall, west_wall]
        np.random.shuffle(walls)

        for wall in walls[0:2]:
            # put a gap at any spot in the wall
            wall[np.random.randint(len(wall))] = 0

        # split the input grid in half
        quadrant_1_2 = [[row[i] for i in range(width_split+1, dimension[0])] for row in empty_grid]
        quadrant_3_4 = [[row[i] for i in range(width_split)] for row in empty_grid]

        # split the halves into four quadrants
        quadrant_1 = [quadrant_1_2[i] for i in range(height_split)]
        quadrant_2 = [quadrant_1_2[i] for i in range(height_split+1, dimension[1])]
        quadrant_3 = [quadrant_3_4[i] for i in range(height_split + 1, dimension[1])]
        quadrant_4 = [quadrant_3_4[i] for i in range(height_split)]

        # recursive calls on each quadrant
        quadrant_1 = generate_maze(quadrant_1, [dimension[0] - width_split - 1, height_split])
        quadrant_2 = generate_maze(quadrant_2, [dimension[0] - width_split - 1, dimension[1] - height_split - 1])
        quadrant_3 = generate_maze(quadrant_3, [width_split, dimension[1] - height_split - 1])
        quadrant_4 = generate_maze(quadrant_4, [width_split, height_split])

        # combine the four quadrants and walls back into one map and return
        quadrant_4_1 = []
        quadrant_3_2 = []
        for four, wall, one in zip(quadrant_4, north_wall, quadrant_1):
            quadrant_4_1.append(four + [wall] + one)
        for three, wall, two in zip(quadrant_3, south_wall[1:], quadrant_2):
            quadrant_3_2.append(three + [wall] + two)

        return quadrant_4_1 + horizontal_wall + quadrant_3_2


not_a_maze = [[0 for _ in range(DIMENSION[0])] for _ in range(DIMENSION[1])]
maze = generate_maze(not_a_maze, DIMENSION)
print maze
