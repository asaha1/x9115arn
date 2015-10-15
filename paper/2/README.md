<h1>i.	Reference to the paper: </h1>
Ruilian Zhao, Micheal R. Lyu, Yinghu Min, 2009. Automatic string test data generation for detecting domain errors. In Journal Software Testing, Verification & Reliability, Volume 20 Issue 3, September 2010, Pages 209-236
<h1>ii.	Most important keywords: </h1>
<b>ii1. Domain Testing:</b> Domain testing is a software testing technique in which selecting a small number of test cases from (usually a nearly infinite) group of test cases. This is used for testing software.
<b>ii2. Dynamic Test data generation:</b> Generation of the test data on the go where the generator intelligently modifies the test data.
<b>ii3. ON-OFF test points:</b> ON test point lies on the given solution predicate border whereas the OFF test point lies just outside the border. They both are as close as possible to check the border points.
<b>ii4. String predicate:</b> In this paper the string predicate border is tested on.
<h1>iii.	Brief Notes: </h1>
<b>iii1. Motivational Statements:</b> A lot of work on domain testing is getting generated to guarantee software quality and reliability. The most expensive step in the testing is test case generation and effective test cases determine the reliability of the software. Manually developing the test data set is expensive, laborious, difficult and error prone. So the paper is based on automatic generation of test data.
<b>iii2. Related Work:</b> The earlier studies which have used ON-OFF test generation has focused only on numeric types and ignored string data. The studies which addressed string test generation used string mutation operators like insertion, deletion and substitution. This study specifically addressed the problem of ON-OFF test data generation on string predicates.
<b>iii3. Informative Visualizations:</b>
<b>iii4. Future Works:</b> The system is currently semi-automated but the aim should be to produce a fully-automated product. If the test string in the predicate is a literal that contains one character then for predicate Max-pre1, the conclusions get invalid. These are the areas where development can be done.
<h1>iv.	Suggested Improvements: </h1>
<b>iv1.</b> The performance of the system can be enhanced to incorporate initial inputs not shorter than the target string and with characters generated randomly.
<b>iv2.</b> For password predicate, the initial input should not be shorter than the target string in the predicate under test. The author states that this trend is found in predicates Max-pre2, random, etc. but doesn’t take this step into account.
<b>iv3.</b> ON-OFF test generation is a heuristic process and therefore the instrumented program has to be executed again in order to evaluate its objective function. The cost of the objective function can be reduced by using algorithms like dynamic programming. This will drastically reduce the running time of the evaluation function.
