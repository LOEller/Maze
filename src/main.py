from graphics import *
from population import Population
from hard_population import HardPopulation

# On the agenda should definitely be to change all of the xranges to range
# which I can do with one vim command but I'll save for later

# TO Do: label groups of MRs that get drawn to the screen with the number of MR
# at that position, generations with really low average fitnesses tend to be really spread out

# This can also save time by not undrawing and re-drawing MRs to the same location,
# we can keep a record of which spots have MRs draw on them and then only draw one
# MR to each space and not have to undraw all the MRs on the same space

# Make a maze here where you put W for the walls and O for the path, and E at
# the end of the maze
maze = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
        ['W', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'W', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'W', 'W', 'O', 'W'],
        ['O', 'O', 'W', 'W', 'W', 'W', 'W', 'O', 'W', 'O', 'W', 'O', 'W', 'W', 'W', 'O', 'W', 'W', 'O', 'W'],
        ['W', 'O', 'W', 'W', 'O', 'O', 'O', 'O', 'W', 'O', 'W', 'O', 'W', 'W', 'W', 'O', 'W', 'W', 'O', 'W'],
        ['W', 'O', 'W', 'W', 'O', 'W', 'W', 'W', 'W', 'O', 'W', 'O', 'W', 'W', 'W', 'O', 'O', 'O', 'O', 'W'],
        ['W', 'O', 'W', 'W', 'O', 'W', 'W', 'W', 'W', 'O', 'W', 'O', 'W', 'W', 'W', 'W', 'W', 'W', 'O', 'W'],
        ['W', 'O', 'W', 'O', 'O', 'W', 'O', 'O', 'O', 'O', 'W', 'O', 'W', 'W', 'W', 'W', 'W', 'W', 'O', 'W'],
        ['W', 'O', 'W', 'O', 'W', 'W', 'O', 'W', 'W', 'W', 'W', 'O', 'W', 'W', 'W', 'W', 'W', 'W', 'O', 'W'],
        ['W', 'O', 'W', 'O', 'W', 'W', 'O', 'W', 'W', 'W', 'W', 'O', 'O', 'O', 'W', 'W', 'O', 'O', 'O', 'W'],
        ['W', 'O', 'W', 'O', 'W', 'W', 'O', 'O', 'O', 'O', 'W', 'W', 'W', 'O', 'W', 'W', 'W', 'W', 'W', 'W'],
        ['W', 'O', 'W', 'O', 'O', 'O', 'W', 'W', 'W', 'O', 'W', 'W', 'W', 'O', 'O', 'O', 'W', 'O', 'O', 'W'],
        ['W', 'O', 'W', 'W', 'W', 'O', 'W', 'W', 'W', 'O', 'W', 'O', 'O', 'O', 'W', 'O', 'W', 'W', 'O', 'W'],
        ['W', 'O', 'W', 'W', 'W', 'O', 'W', 'W', 'W', 'O', 'W', 'O', 'W', 'W', 'W', 'O', 'O', 'O', 'O', 'W'],
        ['W', 'O', 'W', 'W', 'W', 'O', 'O', 'O', 'O', 'O', 'W', 'O', 'W', 'W', 'W', 'O', 'W', 'W', 'W', 'W'],
        ['W', 'O', 'W', 'W', 'W', 'W', 'W', 'W', 'O', 'W', 'W', 'O', 'W', 'W', 'W', 'O', 'W', 'W', 'W', 'W'],
        ['W', 'O', 'W', 'O', 'O', 'O', 'O', 'W', 'O', 'W', 'W', 'O', 'W', 'W', 'W', 'O', 'W', 'W', 'W', 'W'],
        ['W', 'O', 'W', 'O', 'W', 'W', 'O', 'W', 'O', 'O', 'W', 'O', 'O', 'W', 'W', 'O', 'O', 'O', 'O', 'W'],
        ['W', 'O', 'W', 'O', 'W', 'W', 'O', 'W', 'W', 'W', 'W', 'W', 'O', 'W', 'W', 'W', 'W', 'W', 'O', 'W'],
        ['W', 'O', 'O', 'O', 'W', 'W', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'W', 'W', 'W', 'W', 'W', 'O', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'E', 'W']]

# make window and draw the maze
win = GraphWin("Maze Runner", 400, 400)

for j in range(len(maze)):
    for i in range(len(maze[j])):
        r = Rectangle(Point(20*i,20*j), Point(20*i + 20,20*j + 20))
        if (maze[j][i] == "W"):
            r.setFill("black")
        r.draw(win)

# make a new population
# Population(window, maze, starting X pos, starting Y pos, starting direction, end X pos, end Y pos)
population = HardPopulation(win, maze, 0, 2, 0, 18, 19)

# run the simulation for 100 generations
population.advance(100)
