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
        
    MAX_ENERGY = 19609524724
    MIN_ENERGY = 7202
    
    def neighbor(self, state):
        return random.randrange(-1000, 1000) + state
        
    def getEnergy(self, state):
        f1 = self.schafferF1(state)
        f2 = self.schafferF2(state)
        return float(f1 + f2 - self.MIN_ENERGY) / (self.MAX_ENERGY - self.MIN_ENERGY)
        
    def p(self, oldEnergy, newEnergy, temp):
        return math.exp((float(oldEnergy - newEnergy)) / temp)
    
    def simulatedAnnealing(self):
        state = 0
        energy = self.getCumulatedEnergy(state)
        stateBest = state
        energyBest = energy
        k = 0
        kMax = 5
        while k < kMax:
            print "sb = ", stateBest
            print "eb = ", energyBest
            stateNeighbor = self.neighbor(state)
            print "sn =", stateNeighbor
            energyNeighbor = self.getEnergy(stateNeighbor)
            print "en = ", energyNeighbor
            
            if energyNeighbor < energyBest:
                stateBest = stateNeighbor
                energyBest = energyNeighbor
                say("!")
            if energyNeighbor < energy:
                state = stateNeighbor
                energy = energyNeighbor
                say("+")
            elif self.p(energy, energyNeighbor, (1 - float(k) / kMax)) < random.random():
                energy = energyNeighbor
                say("?")
                
            say(".")
            k += 1
            if k % 50 == 0: print "\n", stateBest
            
        return stateBest

if __name__ == '__main__':
    sa = SimulatedAnnealing()
    sa.simulatedAnnealing()