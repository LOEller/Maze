from maze_runner import MazeRunner
import random

# Concrete class implements the Maze Runner API to allow for use with the
# genetic algorithm
class EvolvableMR (MazeRunner):
    def __init__ (self, win, x, y, direction, maze):
        MazeRunner.__init__(self, win, x, y, direction, maze)
        self.fitness = None
        self.chromosome = [None] * 16
        # when we first create the EvolvableMR, give it a random chromosome
        for i in range(1,15):
            self.chromosome[i] = random.choice(
                ['right', 'straight', 'left', 'reverse'])

    # Output: the chromosome index which corresponds to the position this runner
    #          is in
    def getChromeIndex (self):
        directions = self.classifyJuncture()
        index = 0

        if 'right' in directions:
            index += 1
        if 'left' in directions:
            index += 2
        if 'straight' in directions:
            index += 4
        if 'reverse' in directions:
            index += 8

        return index

    def makeDecision (self):
        if self.atEnd():
            return
        elif self.atJuncture():
            self.direction = self.relativeToCardinal(
                self.chromosome[self.getChromeIndex()])

    # Sets the chromosome of this EvolvableMR to implement the wall following
    # algorithm.
    def setWallFollower (self):
        # O state is unreachable: always at least one direction to go in
        self.chromosome[1] = 'right'
        self.chromosome[2] = 'left'
        self.chromosome[3] = 'right'
        self.chromosome[4] = 'straight'
        self.chromosome[5] = 'right'
        self.chromosome[6] = 'straight'
        self.chromosome[7] = 'right'
        self.chromosome[8] = 'reverse'
        self.chromosome[9] = 'right'
        self.chromosome[10] = 'left'
        self.chromosome[11] = 'right'
        self.chromosome[12] = 'straight'
        self.chromosome[13] = 'right'
        self.chromosome[14] = 'straight'
        self.chromosome[15] = 'right'
