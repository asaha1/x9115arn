<h1>i.	Reference to the paper: </h1>
Finding bugs in web applications using dynamic test generation and explicit state model checking. Shay Artzi, Adam Kiezun, Julian Dolby, Frank Tip, Daniel Dig, Amit Paradkar, and Michael D. Ernst.</br>
<h1>ii.	Most important keywords: </h1>
<b>ii1. Web application:</b> These are those types of software based applications which run on a web browser. They are originally written in scripting languages and their control does not flow via simply the code but via the generated HTML text.</br> 
<b>ii2. Failures in HTML: </b> When a problem in HTML is generated this type of error occurs. </br>
<b>ii3. Explicit-state model checking: </b> It is that type of algorithm that reaches only a single level deep in the application. That means it is an algorithm that always starts the checking again from the same initial state and removes the state reached at the end of each execution. </br>
<b>ii4. Static analysis: </b> It is the type of debugging technique which is done before the execution of program. It helps to provide a better understanding of the code. </br>
<h1>iii. Brief Notes: </h1>
<b>iii1. Motivational Statements:</b>
The goal of this paper is to provide a solution for avoiding problems caused by malformed web pages and web script crashes. It does this by using dynamic test generation technique. This is an automated technique which generates input and runs the code, then varies the input to obtain a bug report. </br>
<b>iii2. Tools used: </b>
The prime tool used in the above mentioned test is Apollo. The first step taken by it is to execute the web application with an empty input under test. It records the dependence of control flow on input after each execution. It determines the type of failures that occur, i.e. whether the failures are execution failures or HTML failures. </br>
<b>iii3. Tutorials: </b>
This paper teaches a lot of things. It shows there are two types of errors which could occur in a web application, namely HTML error and execution error. The examples mentioned are in a very organized format in a step by step way for readers with little knowledge on the subject to understand easily. </br>
<b>iii4. Final results. </b>
The tool used in the test obtains a detailed report of the bug or errors which is very beneficial for readers and other researchers. The presence of accurate data and real time examples makes Apollo understandable.
<h1>iv.	Suggested Improvements: </h1>
<b>iv1.</b> One of the very important attributes of javascript is callback, however callback is not widely used in PHP than in javascript. For this reason in the sample program mentioned callback does not affect much, However in the cases where callback function has more effect How well this test acts has to be seen.</br>
<b>iv2.</b> Apollo considers only POST GET and REQUEST as sources for the input parameters.</br>
<b>iv3.</b> In some web applications the Apollo strategy is 8 times better than the randomized strategy where as in some cases it is almost the same. Such difference in performance has to be noted.</br>
<h1>v. Connection to the other papers: </h1>
The first paper was on automated web application testing using search based software engineering. The second paper was on automated domain testing on string predicates. This paper is based on finding bugs by dynamic test generation technique for the domain of dynamic web applications. A tool called Apollo is used to find two kinds of failures - execution failures and HTML failures.