from DE import DE as de
from NSGA2 import NSGA2 as nsga2
from SPEA2 import SPEA2 as spea2
from IntegratedProjectModel_QA import Integrated_project_model_qa as model
from sk import rdivDemo

if __name__ == '__main__':
    optimize = []
    i = 0
    for optimizer in [de, nsga2, spea2]:
        print "Optimizer: %s, " % optimizer.__name__, "Model: %s\n" % model.__name__
        optimize.append([optimizer.__name__] + optimizer(model))
        print ""
        i += 1
    print(rdivDemo(optimize))
