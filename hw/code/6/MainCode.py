from Model import Schaffer, Osyczka2, Kursawe
from SA import SimulatedAnnealing as sa
from MWS import MaxWalkSat as mws

if __name__ == '__main__':
    for model in [Schaffer, Kursawe, Osyczka2]:
        for optimizer in [sa, mws]:
            print "Optimizer: %s, " % optimizer.__name__, "Model: %s\n" % model.__name__
            optimizer(model)
            print ""
