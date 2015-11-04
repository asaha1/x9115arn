<h1>i. Reference to the paper: </h1>
G. Wassermann, D. Yu, A. Chander, D. Dhurjati, H. Inamura and Z. Su, "Dynamic Test Input Generation for Web Applications," Proc. ACM/SIGSOFT Int',l Symp. Software Testing and Analysis, pp. 249-260, 2008.
<h1>ii.	Most important keywords: </h1>
<b>ii1. Generation of constraint selectively:</b>
Generation of constraints in a selective manner is to channelize the focus of generation of constraints to those which are relevant to possible failures.</br>
<b>ii2. Verifications:</b>
It refers to the technique of verifying whether the constraints are satisfied.</br>
<b>ii3. Concolic testing:</b>
A software verification technique which uses both symbolic and concrete executions to generate test inputs to find all the execution paths possible.</br>
<b>ii4. Reliability:</b>
Refers to the ability of the system to perform a specific task for a relatively longer period of time.</br>
<h1>iii. Brief Notes: </h1>
<b>iii1. Motivation: </b>
In the paper the author claims that it is difficult to do static analysis on dynamic features of different scripting languages which results in difficulty by missing out bugs in generated applications using these languages.</br>
<b>iii2. Tutorial materials: </b>
The author has focused only on PHP applications. The author takes an ID and attempts to authenticate the user to perform other actions. If the user’s ID does not appear in the database the program exists with an error message.</br>
<b>iii3. Novelty: </b>
The author comes up with new ways to generate test inputs for the analysis of scripting languages based on previous information.</br>
<b>iii4. Related works: </b>
The goal of the paper is to automatically generate test cases that will achieve a designated code-coverage metric: branch coverage or path coverage. Previous work on concolic testing has helped to automate test input generation for desktop applications written in C or Java [1, 2], but web applications written in scripting languages such as PHP pose different challenges. Test input generation with concolic testing has also been pursued by [3, 4, 5]. 
<h1>iv.	Suggested Improvements:</h1> 
<b>iv1.</b> Six different web applications are chosen by the author, but he forgot to mention why these applications are specifically used. It would have been beneficial if the criteria for selecting application were specified.</br>
<b>iv2.</b>  Major applications chosen in the paper are based on PHP.A wide range of application could have been selected.</br>
<b>iv3.</b> Lack of fully automated implementation could be a problem. The loading of web page and the invoking of analyser is done manually and files written by the analyser must be provided manually to the URL.</br>
<h1>v. Connection to paper one: </h1> 
This paper works on the same PHP applications like the first paper. The applications range from small to medium sized applications.</br>
<h1>References:</h1> 
[1] K. Sen and G. Agha. Cute and jcute : Concolic unit testing and explicit path model-checking tools. In Computer Aided Verification, 18th International Conference (CAV 2006), pages 419–423, 2006. (Tool Paper).</br>
[2] K. Sen, D. Marinov, and G. Agha. Cute: a concolic unit testing engine for c. In Proceedings of the 13th ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE 2005), 2005.</br>
[3] C. Cadar and D. R. Engler. Execution generated test cases: How to make system code crash itself. In Model Checking Software, 12th International SPIN Workshop, pages 2–23, 2005. </br>
[4] C. Cadar, V. Ganesh, P. M. Pawlowski, D. L. Dill, and D. R. Engler. Exe: automatically generating inputs of death. In Proceedings of the 13th ACM Conference on Computer and Communications Security (CCS 2006), pages 322–335, 2006.</br>
[5] M. Costa, M. Castro, L. Zhou, L. Zhang, and M. Peinado. Bouncer: securing software by blocking bad input. In Proceedings of the 21st ACM Symposium on Operating Systems Principles 2007 (SOSP 2007), pages 117–130, 2007.</br>
