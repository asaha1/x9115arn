#Analysis and Optimization of Integrated Project Model Quality Assurance Chain using DE, NSGA2 and SPEA2
-	Arnab Saha (asaha@ncsu.edu)

##Abstract

Software quality is a field of study and practice that describes the desirable attributes of software products. There is a major relationship between product attributes and their impact on business value. Integrated Project Model Quality Assurance Chain is a software model by Abdel-Hamid and Madnick which demonstrates a value-based framework for decision analysis by modeling dependability impact on costs and profit of achieving different reliability levels. In this project, this model was implemented to generate sample values of detected errors and escaped errors. Then the model was optimized to reduce the errors by using DE, NSGA2 and SPEA2 and further a comparison of the optimizers were done on values of each generation of solutions using Scott-Knott algorithm.

##Introduction

Software quality refers to two related but distinct notions that exist wherever quality is defined in a business context – Functional Quality and Structural Quality. Software Functional Quality is the measure of how well the software complies with the given design based on the functional requirements or specifications [1]. On the other hand Software Structural Quality refers to how well the software met the non-functional requirements like robustness or maintainability. The structural quality is usually tested by analyzing the inner structure of the software such as its source code at the unit level as well as the system level. In contrast, functional quality is usually enforced by software testing. 

In this paper we are typically interested in the functional quality which deals with the characteristics of the software. Typically the relative importance of different characteristics or attributes depends on who is assessing the software and what they need or expect from it [2].  Utility can be considered in many ways. Users frequently are concerned about the number and type of failures that occur during usage. Hence, the number of defects is a measure of quality but there are many other possible measures. The Integrated Project Model developed by Abdel-Hamid [2] was used to model the generation, detection, and correction of errors during development. Although the original model consists of 10 sectors as listed below, the Quality Assurance Chain was tested in this model as this is one of the most important sectors of the model.


1. Software Development Sector
2. Enter Project Parameters
3. Planning Sector
4. Human Resources Sector
5. Quality Assurance
6. Manpower Allocation Sector
7. Control
8. Testing
9. Software development Productivity Sector
10. Estimation


<img src="\images\ipm_full.png">


Integrated Project Model: image screen captured from ISEE player

##Background


Evolutionary algorithms or EAs are computer programs that attempt to solve complex problems by mimicking the processes of Darwinian evolution. In an EA a number of artificial creatures search over the space of the problem [3]. They compete continually with each other to discover optimal areas of the search space. It is hoped that over time the most successful of these creatures will evolve to discover the optimal solution. Therefore these algorithms can be used to approximate solutions and optimize different types of problems. 
The optimizers used in this project are Differential Evolution (DE), Non Sorting Genetic Algorithm II (NSGA2) and Strength Pareto Evolutionary Algorithm II (SPEA2). These algorithms are based on Darwinian principles and uses iterative progress, such as growth or development in a population. 


DE was invented by Storn and Price [4]. It is a method that optimizes a problem by iteratively trying to improve a candidate solution with regard to a given measure of quality. DE optimizes a problem by maintaining a population of candidate solutions and creating new candidate solutions by combining existing ones according to its simple formulae, and then keeping whichever candidate solution has the best score or fitness on the optimization problem at hand. DE builds new candidates by extrapolating between members of the current frontier using the algorithm: 
* No needs for frequency tables of better ranges
  * The frontier has the better ranges;
* Pick three things (X,Y,Z);
  * At some probability (called the crossover factor):
  * New = X + f * (Y - Z)


NSGA2 was invented by Srinivas and Deb [5]. The objective of the NSGA algorithm is to improve the adaptive fit of a population of candidate solutions to a Pareto front constrained by a set of objective functions. The algorithm uses an evolutionary process with surrogates for evolutionary operators including selection, genetic crossover, and genetic mutation. The population is sorted into a hierarchy of sub-populations based on the ordering of Pareto dominance. Similarity between members of each sub-group is evaluated on the Pareto front, and the resulting groups and similarity measures are used to promote a diverse front of non-dominated solutions. 


SPEA2 was invented by E.Zitler et al [6]. The objective of the algorithm is to locate and and maintain a front of non-dominated solutions, ideally a set of Pareto optimal solutions. This is achieved by using an evolutionary process (with surrogate procedures for genetic recombination and mutation) to explore the search space, and a selection process that uses a combination of the degree to which a candidate solution is dominated (strength) and an estimation of density of the Pareto front as an assigned fitness. An archive of the non-dominated set is maintained separate from the population of candidate solutions used in the evolutionary process, providing a form of elitism.

##Implementation


The Integrated Project Model Quality Assurance Chain was implemented using the concepts of Domain Specific Language. The model has been implemented using the concepts of stock, flow and auxiliary variables. 
* Stock: A Stock variable is measured at one specific time, and represents a quantity existing at that point in time, which may have accumulated in the past [from lecture notes]. Formally a stock is some entity that is accumulated over time by inflows and/or depleted by outflows. Stocks can only be changed via flows. Mathematically a stock can be seen as an accumulation or integration of flows over time - with outflows subtracting from the stock. Stocks typically have a certain value at each moment of time - e.g. the number of population at a certain moment.
* Flow: A flow variable is measured over an interval of time. Therefore a flow would be measured per unit of time. Flow is roughly analogous to rate or speed in this sense. Usually we can clearly distinguish inflows (adding to the stock) and outflows (subtracting from the stock). Flows typically are measured over a certain interval of time - e.g., the number of births over a day or month.
* Auxiliary: An auxiliary variable is used to store intermediate values that can be calculated based on stocks/flows at the current time. 


<img src="\images\ipm_QA.png">

Integrated Project Model Quality Assurance Chain


As mentioned above, the Quality Assurance chain of the Integrated Project Model was evaluated. Some of the stocks, flows, and auxiliaries in the model are listed below.


| Stocks   |   Flows   |Auxiliaries| 
|-----|-----|-----|
|Tasks_worked, Potentially_detectable_errors, Detected_errors, Reworked_errors_during_devel, Escaped_errors, Cumulative_errors    | SD_rate, QA_rate, Error_generation_rate, Error_escape_rate, Error_detection_rate, rework_rate, Count_detected_errors, generation_rate  | Software_development_rate, Average_qa_delay, Potentially_detectable_errors, DSI_per_task, Multiplier_for_losses, Percent_of_job_actually_worked, Daily_MP_for_QA, Percent_of_job_actually_worked, DSI_per_task, Schedule_pressure, Ratio_of_pros_to_rookies, Software_development_rate, QA_rate, Average#errors_per_task, Daily_mp_for_rework, Multiplier_for_losses, Error_generation_rate, QA_rate, Error_density, Multiplier_due_to_error_density  |


```
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,        NSGA2 ,    0.00  ,  0.00 (*              |              ), 0.00,  0.00,  0.00
   2 ,        SPEA2 ,    0.06  ,  0.06 (     -*        |              ), 0.05,  0.06,  0.11
   2 ,           DE ,    0.07  ,  0.15 (  -----*       |              ), 0.02,  0.07,  0.17
```

```
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,        NSGA2 ,    0.00  ,  0.00 (*              |              ), 0.00,  0.00,  0.00
   1 ,        SPEA2 ,    0.00  ,  0.00 (*              |              ), 0.00,  0.00,  0.00
   2 ,           DE ,    0.02  ,  0.04 ( ----*         |              ), 0.01,  0.02,  0.04
```

```
if __name__ == '__main__':
    optimize = []
    i = 0
    for optimizer in [de, nsga2, spea2]:
        print "Optimizer: %s, " % optimizer.__name__, "Model: %s\n" % model.__name__
        optimize.append([optimizer.__name__] + optimizer(model))
        print ""
        i += 1
    print optimize
    print ""
    print(rdivDemo(optimize))
```









References
1.	Pressman, Scott (2005), Software Engineering: A Practitioner's Approach (Sixth, International ed.), McGraw-Hill Education Pressman, p. 388
2.	T. Abdel-Hamid, and S. Madnick, "Software Project Dynamics: An Integrated Approach", Prentice Hall, NJ, USA, 1990
3.	Gareth Jones. Genetic and evolutionary algorithms, September 1998.
4.	R. Storn, and K. Price, "Differential Evolution: A Simple and Efficient Heuristic for Global Optimization Over Continuous Spaces", in Journal of Global Optimization, vol. 11, no. 4, pages 341-359, December, 1997
5.	K. Deb and S. Agrawal and A. Pratap and T. Meyarivan, "A Fast Elitist Non–dominated Sorting Genetic Algorithm for Multi–Objective Optimization: NSGA–II", Parallel Problem Solving from Nature PPSN VI, 2000.
6.	E. Zitzler and M. Laumanns and L. Thiele, "SPEA2: Improving the strength pareto evolutionary algorithm for multiobjective optimization", in Evolutionary Methods for Design, Optimisation and Control with Application to Industrial Problems (EUROGEN 2001), 2002.
