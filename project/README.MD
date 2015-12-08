<h1>Analysis and Optimization of Integrated Project Model Quality Assurance Chain using DE, NSGA2 and SPEA2</h1>
-	Arnab Saha (asaha@ncsu.edu)

<h1>Abstract</h1>
Software quality is a field of study and practice that describes the desirable attributes of software products. There is a major relationship between product attributes and their impact on business value. Integrated Project Model Quality Assurance Chain is a software model by Abdel-Hamid and Madnick which demonstrates a value-based framework for decision analysis by modeling dependability impact on costs and profit of achieving different reliability levels. In this project, this model was implemented to generate sample values of detected errors and escaped errors. Then the model was optimized to reduce the errors by using DE, NSGA2 and SPEA2 and further a comparison of the optimizers were done on values of each generation of solutions using Scott-Knott algorithm.
<h1>Introduction</h1>
Software quality refers to two related but distinct notions that exist wherever quality is defined in a business context – Functional Quality and Structural Quality. Software Functional Quality is the measure of how well the software complies with the given design based on the functional requirements or specifications [1]. On the other hand Software Structural Quality refers to how well the software met the non-functional requirements like robustness or maintainability. The structural quality is usually tested by analyzing the inner structure of the software such as its source code at the unit level as well as the system level. In contrast, functional quality is usually enforced by software testing. 
In this paper we are typically interested in the functional quality which deals with the characteristics of the software. Typically the relative importance of different characteristics or attributes depends on who is assessing the software and what they need or expect from it [2].  Utility can be considered in many ways. Users frequently are concerned about the number and type of failures that occur during usage. Hence, the number of defects is a measure of quality but there are many other possible measures. The Integrated Project Model developed by Abdel-Hamid [2] was used to model the generation, detection, and correction of errors during development. Although the original model consists of 10 sectors as listed below, the Quality Assurance Chain was tested in this model as this is one of the most important sectors of the model.
i.	Software Development Sector
ii.	Enter Project Parameters
iii.	Planning Sector
iv.	Human Resources Sector
v.	Quality Assurance
vi.	Manpower Allocation Sector
vii.	Control
viii.	Testing
ix.	Software development Productivity Sector
x.	Estimation
<img src="\images\ipm_full.png">
<h1>Background:</h1>
Evolutionary algorithms or EAs are computer programs that attempt to solve complex problems by mimicking the processes of Darwinian evolution. In an EA a number of artificial creatures search over the space of the problem [3]. They compete continually with each other to discover optimal areas of the search space. It is hoped that over time the most successful of these creatures will evolve to discover the optimal solution. Therefore these algorithms can be used to approximate solutions and optimize different types of problems. 
The optimizers used in this project are Differential Evolution (DE), Non Sorting Genetic Algorithm II (NSGA2) and Strength Pareto Evolutionary Algorithm II (SPEA2). These algorithms are based on Darwinian principles and uses iterative progress, such as growth or development in a population. 
DE was invented by Storn and Price [4]. It is a method that optimizes a problem by iteratively trying to improve a candidate solution with regard to a given measure of quality. DE optimizes a problem by maintaining a population of candidate solutions and creating new candidate solutions by combining existing ones according to its simple formulae, and then keeping whichever candidate solution has the best score or fitness on the optimization problem at hand. DE builds new candidates by extrapolating between members of the current frontier using the algorithm: 
-	No needs for frequency tables of better ranges
o	The frontier has the better ranges;
-	Pick three things (X,Y,Z);
-	At some probability (called the crossover factor):
o	New = X + f * (Y - Z)
NSGA2 was invented by Srinivas and Deb [5]. The objective of the NSGA algorithm is to improve the adaptive fit of a population of candidate solutions to a Pareto front constrained by a set of objective functions. The algorithm uses an evolutionary process with surrogates for evolutionary operators including selection, genetic crossover, and genetic mutation. The population is sorted into a hierarchy of sub-populations based on the ordering of Pareto dominance. Similarity between members of each sub-group is evaluated on the Pareto front, and the resulting groups and similarity measures are used to promote a diverse front of non-dominated solutions. 
SPEA2 was invented by E.Zitler et al [6]. The objective of the algorithm is to locate and and maintain a front of non-dominated solutions, ideally a set of Pareto optimal solutions. This is achieved by using an evolutionary process (with surrogate procedures for genetic recombination and mutation) to explore the search space, and a selection process that uses a combination of the degree to which a candidate solution is dominated (strength) and an estimation of density of the Pareto front as an assigned fitness. An archive of the non-dominated set is maintained separate from the population of candidate solutions used in the evolutionary process, providing a form of elitism.

'''
Gen 01 | +..++??++.+?.++..+++++++....+++....+?++.....?+.+++++.+..++.+..+++....+++...+.++..++.+++..+.+..+....+ 
Gen 02 | .+..+++.+.?++.++.+.....+.+..+?.++.?+?..++.+..+.+.?.+...++....++.++++.++..++..+.++...++?.....?+..++.+ 
Gen 03 | ?.+.....?+++...+...+.....+?.+.+.+.+.+..++.......++.+.............+++.+.....+.+...+..++.....?+?.++.++ 
Gen 04 | +.?..++.+++++...+.+.......+.+++.++.+..+?+++...!...+..+...+..+......++++....+...+...?.....+.+++.....+ 
Gen 05 | +..?+++.+?.+++...+..+..?..?+.+++.+.!..?.?...+..+..++..++.+..+?.....+.+++.++.?..+..+++....+.+..+.+.++ 
Gen 06 | .?+..+.+.+.....+++.+.........+++.+..++.?+..+....++.+++.....+...++..+?++...+.++........++...+..+?..+? 
Gen 07 | .+?....++.+..+..+.....+.+.+?.+?..?+..?+?....++?.+......++...+++.+.?......+..??...++...++.+...?.....+ 
Gen 08 | ..+....+++.+....++...+.+..+.+.+++.....+.+.+++++?......?..+...+....+.++.+.+.......+....+.......+++.+. 
Gen 09 | .+..+..+...........+...++.++......+...++?..++.........+++..?.....+....++.....?.....+..+........+.... 
Gen 10 | .?..?+.........+?.+...........??.+....+....+..+.+..+................+++......+++++.+..+++.+.+++.+... 
Gen 11 | +.+++++.+...++.......?..++.+..++.+..+++.+...?+......+++...+...++..?...+...+..+...........++.....++.? 
Gen 12 | +.+.+....+.....+....?+.?..++.++.?+...++...??+...+.+...?.+.+.+....+....+.....++..........?....??..++. 
Gen 13 | +..+..++..........+...++..+...+.....+......+...?+.......+..++?+....+.++.....++..+++.....+......+.... 
Gen 14 | .......+?.......++.+++.++..+.+..+.+!..+++...?....+..+..+.....++.....+....?.+.....+++.+.........++.?+ 
Gen 15 | ++.+...+++.........+.++.++.+.+.+.+..+....+++...+.+.........+?.....+.+....+.+...+++....++.++.+....?.. 
Gen 16 | ..?+..+..+.+?+...++.....+?....+..?.!..+.+.++.+...+....+.+...........+.+.+.+?..++...++.............+. 
Gen 17 | .?..+.+++?.........+.+...+......+?....++++..........+......?++....+.+...+....+......+.+?+++...+....+ 
Gen 18 | ..++.?+.+.+.++.+.+?.......+.?.+..+......+.+.+?..+?............+.....+?+.+..+.+....+..+..+.!+.....?.. 
Gen 19 | ........++..+..+.+.++++......+...?..++.......?....?+.....?..+.++..+.?.?...+...?..+.+..?...?..++....+ 
Gen 20 | +....+..++..+++.+.+..++.....++.++....+..+....+?++....?..+..+++.+.+?.+.++...+.+.........+.+..+......+ 
Gen 21 | ...+.+...+.+.++++..?+....+.+....+?+........+...?.+++.....+..+...?......+..+..+.+...++..+..?.......+. 
Gen 22 | .+?.++............+...+.................+++..++..+..+..+.+............++.++.+++++.+++++.+.?+..++.... 
Gen 23 | ?..+.........++.++.....++.+.......+........?...?...........+.........+.....+?++..+.++..?+....+?..+.. 
Gen 24 | .+?..+?..+....++..+...+...+.++..++.++....+++......?.?..+.?...+....+.+......+..++.....?+.++...+.....+ 
Gen 25 | ++................+.+++..+..+.+...?..+....+..+..............?...+..........++...+..+....+....++....+ 
Gen 26 | .......+.+.+...++...+...+..+........+....?+........+.+.....+++...++..+.+....?+...++......+!?........ 
Gen 27 | ......+....??..++.+....+.?...+.+.....+...+...+....+.+.?...+...+.++?........++.+.++...+......++?...?+ 
Gen 28 | ..+.++.+.+.....+......++...++.+...+.....++....+.+....+.++......+..++...+.?.++.....?+..+..+.+..?.+... 
Gen 29 | +?...+.+.....++.++...+.+........?.....++++..........+....+.....++........++........++.+.....+..+?.+. 
Gen 30 | ...?......?+.........++.+.++.++.......+..+..+.....+.....?++.+...+....+.++++.+...++.+...+.....?+.++++ 
Gen 31 | .....++.......++.....++....+..++.+..+...++?....+++.+......+...?.++.?.++.?.+...+....?....+...+......+ 
Gen 32 | ..+...++.+?+....++.....?.......+...+....+......+......?.+...+?+...++..++.?.........?.?+?....?.?+++.. 
Gen 33 | +++++.+....++.++?...?.....+............+....+...+......+.+..+...?.+.+....++?....+....+.?....+..??+.. 
Gen 34 | ..+...+.+......+...+++....+.+.........?+++...............+.?...++.+.+..+.?.....+.+.+..++!...+.+...+. 
Gen 35 | ....+....+......+...?....?....?.....+..+....+....+.+........+..........++?.....+...?+.?....+.?..?... 
Gen 36 | ++..?.......?.+?+..?+..?.?.....??...+.....+.+..+...+?.......+......?....++.....?...++.++.+....?..++. 
Gen 37 | .+..+.?.+...+..+...+...+?.............+.+.+?+......+?.?+.....?+...+...++......+....?+.......+.?+?.+. 
Gen 38 | .+.............+.+..+...+??.+.+...........+.......+.+.?.....?+.....?+.......++++..?.+.++.+?...+.+.?+ 
Gen 39 | .+..+?++..+.....+++.?.....+.?..+.....?+...+.?+++.++.......+..?++......+.....+++.........?..+.+...... 
Gen 40 | +.........+++.+.++.....+.....++...+..+.++..?.?..+...+..++.?+..+......+++?......+..+....+....+??.?.+. 
Gen 41 | .+.........+..+.+.+...++..+?+....+.??......?+.......+++.++.??....++.+++...........+........+..+..... 
Gen 42 | ...+...+++?.....+......?.+......?...+...............++.+..+??.+...+...+.?....++.?.......!+.+....+..+ 
Gen 43 | ...+......?..+.++.........++?....+..+.?+......+......++.+....+....++.............+.+...?.....+.++..+ 
Gen 44 | +.......+.......++.+...?......+..+.....+.........+++?.........+....++...+...........++......+......+ 
Gen 45 | +......?++...+..+..++..+.+..??.?.....?.+++...+.......+......++..?.+.........?..++....+...++..++....+ 
Gen 46 | ..?...........?..+...++.++....+....................+............??.+...+.++.?+...?+....+.+....+..... 
Gen 47 | +...++..?....++.+.......+..++...+........+......++...+.....+++...+.....+...??........+...+.++...??.. 
Gen 48 | .......+..+.+.?+.......+..++......+......++..!..++.+..+...+..?+.......!.......+.++...++.+.........?+ 
Gen 49 | +.+............?++.+.+...+.+..++++.+.?........+.....+....??.....?.....?...........+...++.....+....?. 
Gen 50 | ...++....?+...+.+..++..+....?+......?+?+?..+...+?+...+......?++.+..++.!............?.....+++..+..... 
'''











References
1.	Pressman, Scott (2005), Software Engineering: A Practitioner's Approach (Sixth, International ed.), McGraw-Hill Education Pressman, p. 388
2.	T. Abdel-Hamid, and S. Madnick, "Software Project Dynamics: An Integrated Approach", Prentice Hall, NJ, USA, 1990
3.	Gareth Jones. Genetic and evolutionary algorithms, September 1998.
4.	R. Storn, and K. Price, "Differential Evolution: A Simple and Efficient Heuristic for Global Optimization Over Continuous Spaces", in Journal of Global Optimization, vol. 11, no. 4, pages 341-359, December, 1997
5.	K. Deb and S. Agrawal and A. Pratap and T. Meyarivan, "A Fast Elitist Non–dominated Sorting Genetic Algorithm for Multi–Objective Optimization: NSGA–II", Parallel Problem Solving from Nature PPSN VI, 2000.
6.	E. Zitzler and M. Laumanns and L. Thiele, "SPEA2: Improving the strength pareto evolutionary algorithm for multiobjective optimization", in Evolutionary Methods for Design, Optimisation and Control with Application to Industrial Problems (EUROGEN 2001), 2002.
