import random
from maze_runner import MazeRunner

# Concrete class implements the Maze Runner API with random decision making
class RandomMR (MazeRunner):
    # Pick a random direction
    def makeDecision (self):
        if self.atEnd():
            return
        if self.atJuncture():
            self.direction = self.relativeToCardinal(
                random.choice(['right', 'left', 'straight', 'reverse']))
