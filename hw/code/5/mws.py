import random, sys

bounds = list()
bounds.append([1, 10])
bounds.append([1, 10])
bounds.append([1, 5])
bounds.append([0, 6])
bounds.append([1, 5])
bounds.append([0, 10])

class MWS(object):
    maxtries = 1000
    maxchanges = 25
    emax = 1
    emin = 0
    prob = 0.5
    
    # maxwalksat algorithm
    def mws(self):
        solution = self.randomAssignment()
        energy = self.energy(solution)
        snext = solution[:]
        sbest = solution[:]
        ebest = energy
        for i in range(self.maxtries):            
            if i % 4 == 0:
                print "\n", i, " | ",
                
            for j in range(self.maxchanges):  
                if energy >= self.emax + 100:
                    return solution, energy
                
                # select which variable to mutate
                c = random.randint(0, 5)
                snext = solution[:]
                if self.prob < random.random():
                    print "?",
                    snext = self.tweak(c, snext)
                else:
                    snext = self.mutate(c, snext)
                    
                if snext[c] == solution[c]:
                    print ".", 
                else:
                    print "+",
                
                solution = snext                    
                energy = self.energy(solution)
                if energy > ebest:
                    ebest = energy
                    sbest = solution
                    
            solution = self.randomAssignment()
            energy = self.energy(solution)
#             print solution, energy
        energy = self.energy(solution)
        return sbest, ebest
    
    #returns a random solution
    def randomAssignment(self):
        currentSolution = list()
        # generates a solution
        for i in range(6):
            currentSolution.append(randomWithinBounds(bounds[i]))
        # checks the constraints
        currentSolution = constraintsG1G2(currentSolution)
        currentSolution = constraintsG3G4(currentSolution)
        currentSolution = constraintsG5G6(currentSolution)
        
        return currentSolution
    
    #change a random variable
    def tweak(self, pos, sol):
        sol[pos] = randomWithinBounds(bounds[pos])
        #check the constraints
        sol = constraintsG1G2(sol)
        sol = constraintsG3G4(sol)
        sol = constraintsG5G6(sol)
        return sol
    
    #change a variable in steps to maximize the energy
    def mutate(self, var, sol):
        steps = 10
        best_x = sol[var]
        best_score = self.energy(sol)
        
        x_min, x_max = bounds[var]
        x = x_min
        
        step = (float(x_max) - x_min)/10
        for i in range(steps - 1):
            sol[var] = x
            
            temp_energy = self.energy(sol)
            if temp_energy > best_score:
                best_x = x
                best_score = temp_energy
            x = x + step
        # todo put the best x in the solution and return it
        sol[var] = best_x        
        return sol
        
        
    #returns the energy for a solution
    def energy(self, x):
        f1, f2 = osyczka2(x)
        e = f1 + f2
        return e 
        
    # runs for 1000 times to find max and min energy
    def mockRun(self):
        emin = sys.maxint
        emax = - sys.maxint - 1
        
        for i in range(1000):
            s = self.randomAssignment()
            e = self.energy(s)
            if emin > e:
                emin = e
            if emax < e:
                emax = e
                sbest = s
        
        print sbest, emax, emin
        self.emax = emax
        self.emin = emin

# returns a random number within the bounds
def randomWithinBounds(bounds):
    return ((bounds[1] - bounds[0]) * random.random()) + bounds[0]

# takes an list x[6] as input and returns a tuple (f1, f2)
def osyczka2(x):
    f1 = -((25*(x[0] - 2) ** 2 + (x[1] - 2) ** 2 + (x[2] - 1) ** 2)*(x[3] - 4)**2 + (x[4] - 1)**2)
    f2 = sum([x[i] ** 2 for i in range(6)])
    return f1, f2

def constraintsG1G2(x):
    while (x[0] + x[1] - 2 <= 0) or (6 - x[0] - x[1] < 0) or (2 - x[1] - x[0] > 0):
        x[0] = randomWithinBounds(bounds[0])
        x[1] = randomWithinBounds(bounds[1])
    return x
        
def constraintsG3G4(x):
    while ((4 - (x[2] - 3) ** 2 - x[3]) < 0):
        x[2] = randomWithinBounds(bounds[2])
        x[3] = randomWithinBounds(bounds[3])
    return x

def constraintsG5G6(x):
    while 0 > (x[4] - 3) ** 3 + x[5] - 4:
        x[4] = randomWithinBounds(bounds[4])
        x[5] = randomWithinBounds(bounds[5])
    return x   

a = MWS()
a.mockRun()
print "\nBest solution is " + str(a.mws())