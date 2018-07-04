from graphics import *
from abc import ABCMeta, abstractmethod

# An abstract class for the general maze runner API
class MazeRunner:
    __metaclass__ = ABCMeta

    def __init__(self, win, x, y, direction, maze):
        self.win = win
        self.x = x
        self.y = y
        self.gObject = Circle(Point(10 + self.x*20, 10 + self.y*20), 10)
        self.maze = maze
        self.direction = direction

    # Changes the runner's direction
    @abstractmethod
    def makeDecision (self): pass

    def draw (self, color):
        self.gObject = Circle(Point(10 + self.x*20, 10 + self.y*20), 10)
        self.gObject.setFill(color)
        self.gObject.draw(self.win)

    def undraw (self):
        self.gObject.undraw()

    # Output: a 4 letter code of W and O indicating the 4 positions around this
    #         maze runner
    def getPosition (self):
        east = self.maze[self.y][self.x + 1]
        west = self.maze[self.y][self.x - 1]
        north = self.maze[self.y - 1][self.x]
        south = self.maze[self.y + 1][self.x]
        return east + south + west + north

    # Output: true if this maze runner is at a juncture, false otherwise
    def atJuncture (self):
        junctures = ['OWWW', 'WOWW', 'WWOW', 'WWWO', 'OOWW', 'OWWO', 'WOOW',
                     'WWOO', 'OOOO', 'WOOO', 'OWOO', 'OOWO', 'OOOW']
        return self.getPosition() in junctures

    # Output: A code giving the possible choices in terms of relative directions
    #         for this juncture, ie a string with any combination of: 'right',
    #         'straight', 'left', 'reverse'
    def classifyJuncture (self):
        passages = []

        for i, char in enumerate(self.getPosition()):
            if char == 'O' or char == 'E':
                passages.append(i)

        if self.direction == 0:
            directions = ['straight', 'right', 'reverse', 'left']
        elif self.direction == 1:
            directions = ['left', 'straight', 'right', 'reverse']
        elif self.direction == 2:
            directions = ['reverse', 'left', 'straight', 'right']
        elif self.direction == 3:
            directions = ['right', 'reverse', 'left', 'straight']

        result = ''
        for x in passages:
            result = result + directions[x]
        return result

    # Is the maze runner in the ending position?
    def atEnd (self):
        return self.maze[self.y][self.x] == 'E'

    # Converts a relative direction like 'right' or 'straight' into a cardinal
    # direction 0-3 (which correspond to East, South, West, North)
    def relativeToCardinal (self, relDir):
        if relDir == 'right':
            res = [1, 2, 3, 0]
            return res[self.direction]
        elif relDir == 'left':
            res = [3, 0, 1, 2]
            return res[self.direction]
        elif relDir == 'straight':
            return self.direction
        elif relDir == 'reverse':
            res = [2, 3, 0, 1]
            return res[self.direction]

    # Tries to move the runner according to its current direction, if that
    # would move into a wall, it returns false
    def move (self):
        if self.direction == 0:
            if self.maze[self.y][self.x + 1] == 'W':
                return False
            self.x += 1
        if self.direction == 1:
            if self.maze[self.y + 1][self.x] == 'W':
                return False
            self.y += 1
        if self.direction == 2:
            if self.maze[self.y][self.x - 1] == 'W':
                return False
            self.x -= 1
        if self.direction == 3:
            if self.maze[self.y - 1][self.x] == 'W':
                return False
            self.y -= 1
        return True
