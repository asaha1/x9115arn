from DE import DifferentialEvolution as de
from NSGA2 import NSGA2 as nsga2
from IntegratedProjectModel_QA import integrated_project_model_qa as model

if __name__ == '__main__':
        for optimizer in [de, nsga2]:
            print "Optimizer: %s, " % optimizer.__name__, "Model: %s\n" % model.__name__
            optimizer(model)
            print ""