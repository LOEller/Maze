from MazeRunner import MazeRunner

# Concrete class implements the MazeRunner API following the wall-follower
# maze solving algorithm
class WallFollowerMR (MazeRunner):
    # If we can move to the ending spot from where we are, then do so, otherwise
    # use the wall-following algorithm to pick a new direction
    def makeDecision (self):
        if self.atEnd():
            return
        if 'E' in self.getPosition():
            self.direction = self.getPosition().index('E')
        if self.atJuncture():
            directions = self.classifyJuncture()
            if 'right' in directions:
                self.direction = self.relativeToCardinal('right')
            elif 'straight' in directions:
                self.direction = self.direction
            elif 'left' in directions:
                self.direction = self.relativeToCardinal('left')
            elif 'reverse' in directions:
                self.direction = self.relativeToCardinal('reverse')
