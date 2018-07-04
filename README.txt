MAZE

A framework for the genetic algorithm using maze solvers, written in Pure python. I use graphics.py, made by John Zelle for drawing
the maze. http://mcsp.wartburg.edu/zelle/python/graphics.py

The code includes a script, Main.py, for running a simulation. In this file you may specify the design of a maze, and the number of generations.
A planned feature is to include parameters for the genetic algorithm in this file.

There is a Population class which includes code for running the maze solvers through the maze and creating the next generation. The fitness
of an individual is determined by its distance to the end of the maze after either finishing the maze, or completing 1000 moves.

There is a small class hierarchy for the maze solvers themselves. There is an abstract class, MazeRunner, which defines an API for any maze solver.
Then, there are three classes which implement the API, RandomMR, WallFollowerMR, and EvolvableMR.

The EvolvableMR class contains a chromosome which is operated on by the genetic algorithm. The chromosome consists of an individual's decision of 
direction to choose at every possible maze juncture. 

The RandomMR is a maze solver which makes random decisions, and the WallFollowerMR implements the common wall following algorithm to solve any 
possible maze.

The intent of the genetic algorithm is to evolve EvolvableMRs that perform better than RandomMRs, and approach the abilities of WallFollowrMRs.

I have been using population sizes of 100, and to date, the best average fitness for any generation is 4.

The scheme for the genetic algorithm used in this implementation is inspired by the MATLAB genetic algorithm function and can be found here:
https://www.mathworks.com/help/gads/how-the-genetic-algorithm-works.html. This is a great general resource for learning about GA.

Should anyone find this code and want to contribute, I enthusiastically welcome it!
