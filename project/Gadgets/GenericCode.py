from Model import Schaffer, Osyczka2, Kursawe
from SA import SimulatedAnnealing as sa
from MWS import MaxWalkSat as mws
from DE import DifferentialEvolution as de
from NSGA2 import NSGA2 as nsga2

if __name__ == '__main__':
    for model in [Schaffer, Kursawe, Osyczka2]:
        for optimizer in [sa, mws, de, nsga2]:
            print "Optimizer: %s, " % optimizer.__name__, "Model: %s\n" % model.__name__
            optimizer(model)
            print ""
