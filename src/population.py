from evolvable_maze_runner import EvolvableMR
import math
import copy
import random
import copy

# Handles all genetic algorithm code
class Population:
    def __init__ (self, win, maze, startX, startY, direction, endX, endY):
        self.win = win
        self.maze = maze
        self.dir = direction
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
        self.population = [None] * 100
        self.averageFitness = self.distance(self.startX, self.startY, self.endX, self.endY)
        for i in xrange(100):
            self.population[i] = EvolvableMR(win, startX, startY, direction, maze)

    # Runs the simulation on this population
    def advance(self, generations):
        drawn_population = copy.copy(self)
        for _ in range(generations):
            self.runMazeSimulation()
            self.stats()
            self.newGeneration()
            # only draw new record-fitness populations
            if (self.averageFitness < drawn_population.averageFitness):
                drawn_population.undrawAll()
                drawn_population = copy.copy(self)
                drawn_population.drawAll()

    # Moves each maze runner in the population through the maze until a max
    # number of moves are made, or the maze runner reaches the end
    def runMazeSimulation (self):
        for i in xrange(100):
            count = 0
            while (not self.population[i].atEnd()) and (count < 1000):
                self.population[i].move()
                self.population[i].makeDecision()
                count += 1
            self.setFitness(self.population[i])

    # Computes the distance between two points (x1,y1) and (x2,y2)
    def distance (self, x1, y1, x2, y2):
        return math.floor(math.sqrt(
            (x2-x1)**2 +
            (y2-y1)**2))

    # Sets the fitness field of the inputted EvolvableMR
    def setFitness (self, MR):
        MR.fitness = self.distance(MR.x, MR.y, self.endX, self.endY)

    # Output: the index of the most fit maze runner in the population
    def findBestMR (self):
        leastIndex = 0
        for i in xrange(100):
            if self.population[i].fitness < self.population[leastIndex].fitness:
                leastIndex = i
        return leastIndex

    # Input: 2 EvolvableMRs
    # Output: 1 EvolvableMR which is the result of crossing over the two inputs
    def crossover (self, parent1, parent2):
        crossPoint = random.randint(1, 15)
        result = EvolvableMR(self.win, self.startX, self.startY, self.dir, self.maze)
        for i in range(1, 15):
            if i <= crossPoint:
                result.chromosome[i] = parent1.chromosome[i]
            elif i > crossPoint:
                result.chromosome[i] = parent2.chromosome[i]
        return result

    # Input: a maze runner
    # Output: this maze runner with a randomly selected index set to a random
    #         direction
    def mutate (self, MR):
        result = copy.copy(MR)
        index = random.randint(1, 15)
        result.chromosome[index] = random.choice(
            ['right', 'straight', 'left', 'reverse'])
        return result

    # Creates the next generation of maze runners:
    # The most fit 25 MRs are 'elite' and copy into the next generation
    # One mutated copy of each elite also survives to the next generation
    # The middle 50 MRs each produce 1 offspring with a randomly chosen MR
    # also among the middle 50
    # The 25 least fit maze runners die
    def newGeneration (self):
        self.population = sorted(self.population, key = lambda x: x.fitness)
        elites = self.population[:25]
        mutatedElites = [None] * 25
        for i in xrange(25):
            mutatedElites[i] = self.mutate(elites[i])
        parents = self.population[25:75]
        children = [None] * 50
        for i in xrange(50):
            spouseIndex = random.randint(0,49)
            while spouseIndex == i:
                spouseIndex = random.randint(0,49)
            children[i] = self.crossover(parents[i], parents[spouseIndex])
        self.population = elites + mutatedElites + children

    # prints out some statistics for the fitness of this population
    def stats (self):
        fitnesses = [x.fitness for x in self.population]
        print('Total fitness: ' + str(sum(fitnesses)) + ' Average Fitness: ' +
            str(sum(fitnesses)//100))
        self.averageFitness = sum(fitnesses)//100

    def drawAll (self):
        for i in xrange(100):
            self.population[i].draw('blue')

    def undrawAll (self):
        for i in xrange(100):
            self.population[i].undraw()

# Genetic Algorithm Reference
# (see https://www.mathworks.com/help/gads/how-the-genetic-algorithm-works.html)
