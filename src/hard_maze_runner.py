from maze_runner import MazeRunner
import random

# Concrete class implements the Maze Runner API to allow for use with the
# genetic algorithm
class HardMR (MazeRunner):
    def __init__ (self, win, x, y, direction, maze):
        MazeRunner.__init__(self, win, x, y, direction, maze)
        self.fitness = None
        self.chromosome = [None] * 64
        # when we first create the EvolvableMR, give it a random chromosome
        for i in range(1,63):
            self.chromosome[i] = random.choice(
                ['right', 'straight', 'left', 'reverse'])

    # Output: the chromosome index which corresponds to the position this runner
    #          is in
    def getChromeIndex (self):
        pose = self.getPosition()
        index = 0

        for i, char in enumerate(pose):
            if char == 'O' or char == 'E':
                index += 2^i

        # maps it to the correct chromosome index out of 63
        return index + (self.direction * 16)

    def makeDecision (self):
        if self.atEnd():
            return
        elif self.atJuncture():
            self.direction = self.relativeToCardinal(
                self.chromosome[self.getChromeIndex()])


