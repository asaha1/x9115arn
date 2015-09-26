import random
import sys
import math

def say(x): 
    sys.stdout.write(str(x)); sys.stdout.flush()

class SimulatedAnnealing(object):
    MIN_X = -10 ** 5
    MAX_X = 10 ** 5 + 1
    
    def __init__(self):
        self.minEnergy = self.MAX_X
        self.maxEnergy = self.MIN_X
    
    def schafferF1(self, x):
        return x ** 2
        
    def schafferF2(self, x):
        return (x - 2) ** 2

    def generateRandomX(self):
        return random.randrange(self.MIN_X, self.MAX_X)
        
    def getCumulatedEnergy(self, x):
        return self.schafferF1(x) + self.schafferF2(x)
        
    def baselineStudy(self):
        for i in range(100):
            currentEnergy = self.getCumulatedEnergy(self.generateRandomX())
            if currentEnergy < self.minEnergy:
                self.minEnergy = currentEnergy
            if currentEnergy > self.maxEnergy:
                self.maxEnergy = currentEnergy
        print "Min energy = " + str(self.minEnergy)
        print "Max energy = " + str(self.maxEnergy)
        
    MAX_ENERGY = 19609524724.0
    MIN_ENERGY = 7202.0
    
    def neighbor(self, state):
        return random.randrange(-1000, 1000) + state
        
    def getEnergy(self, state):
        return (self.getCumulatedEnergy(state) - self.MIN_ENERGY) / (self.MAX_ENERGY - self.MIN_ENERGY)
        
    def probability(self, oldEnergy, newEnergy, temp):
        prob = math.exp((oldEnergy - newEnergy) / temp)
        #say(prob)
        return prob
    
    def simulatedAnnealing(self):
        state = self.MAX_X
        energy = self.getEnergy(state)
        stateBest = state
        energyBest = energy
        k = 1.0
        kMax = 1000
        while k < kMax:
            if k % 25 == 0: 
                say("\n") 
                say('%04d'%k)
                say(',')
                say(stateBest)
            stateNeighbor = self.neighbor(state)
            energyNeighbor = self.getEnergy(stateNeighbor)
            
            if energyNeighbor < energyBest:
                stateBest = stateNeighbor
                energyBest = energyNeighbor
                say("!")
                
            if energyNeighbor < energy:
                state = stateNeighbor
                energy = energyNeighbor
                say("+")
            elif self.probability(energy, energyNeighbor, k / kMax) - 0.1 < random.random():
                state = stateNeighbor
                energy = energyNeighbor
                say("?")
                
            say(".")
            k += 1
            
            
        return stateBest

if __name__ == '__main__':
    sa = SimulatedAnnealing()
    sa.simulatedAnnealing()
    print ""