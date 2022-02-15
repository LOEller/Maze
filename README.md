# Maze

(An old project of mine, not under active development but recently updated to work with python 3)


```mermaid
  graph TD;
      A-->B;
      A-->C;
      B-->D;
      C-->D;
```

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

TO DO:
- My publication about this project will be divided into two main experiments, one where there are 4^15 possible maze
  runners in the search space, and one where there are 4^60. Within each section, I explore various parameters for the
  evolution and the results for that one.
- As it is now, there are 4^15 possible maze runners that this program could evolve, so I want to see if it is possible to
  expand the search space. At the moment, my program does the work of computing possible relative directions (eg. left)
  from the 4 surrounding maze spaces and the runner's direction. If I took out this step, then there could instead be
  60 (!) chromosome positions because there can be block or no block in each of 4 spaces, and the direction can be one
  of 4 things. So there would be a total of 4^60 possible maze runners, so that would be an even stronger result
- so that only took a minute, now there is a HardPopulation and HardMR class which implement that thing
- DEFINITELY use matlibplot to look at the fitnesses!



