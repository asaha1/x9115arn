<h1>i.	Reference to the paper: </h1>
William G.J. Halfond, Saswat Anand, and Alessandro Orso. Precise Interface Identification to Improve Testing and Analysis of Web Applications. In ISSTA ’09, pages 285–296, 2009
<h1>ii.	Most important keywords: </h1>
<b>ii1.</b> Interface identification: The interface execution is dependent on the input parameters and the flow of execution therefore varies at runtime for web based applications.</br>
<b>ii2.</b> Symbolic execution: A program operates on symbolic inputs that can represent arbitrary values and at any point in the execution variables dependent on the input are represented as algebraic expressions over the symbolic input values. </br>
<b>ii3.</b> Path Condition (PC): PC expresses constraints on the symbolic inputs that must be satisfied in order for execution to reach a specific point in the program.</br>
<b>ii4.</b> Web crawling: It is a common approach to identify accepted interfaces. In this approach, a program called the web spider visits and analyses web pages to discover links to other pages till there are no new links to visit. This information is used to infer interface information about the individual components.</br>
<h1>iii. Brief Notes: </h1>
<b>iii1.</b> Motivational statements: The components of a dynamic web application communicate extensively via their interfaces to generate the dynamic content. In web applications these interfaces are not implicitly defined and vary at runtime. Automated quality assurance is necessary for ensuring quality in these applications.</br>
<b>iii2.</b> Related Work: Many approached to interface identification has been made. Most of them rely on developer provided interface specifications. Ricca and Tonella uses developer-provided UML models [1], Jian and Liu use a formal specification [2], and Andrews, Offutt, and Alexander [3] use finite state machines. An approach by Elbaum and colleagues [4] uses a series of requests to an application to identify its interfaces and infer constraints on the IPs of the interfaces by analyzing responses to the request. A spider by Huang and colleagues [5] uses sophisticated heuristics to more effectively and thoroughly explore a web app. lication.</br>
<b>iii3.</b> Informative visualizations:</b> </br>
<b>iii4.</b> Delivery Tools: The authors has developed a tool in Java called WAM-SE (Web Application Modeling with Symbolic Execution) to evaluate their approach. It consists of three modules:</br>
Transform- is used to implement the symbolic transformation. The input to this module is the bytecode of the web application and the specification of program entities to be considered symbolic (in this case, symbolic strings).</br>
SE Engine- implements the symbolic execution. The input to this module is the bytecode of the transformed web application, and the output is the set of all PCs and corresponding symbolic states for each component in the application.</br>
PC Analysis- implements the analysis. The input to this module is the set of PCs and symbolic states for each component in the application, and the output is the set of IDCs and accepted interfaces. The module iterates over every PC and symbolic state, identies the accepted interfaces, and associates the constraints on each IP with its corresponding accepted interface.</br>

iv.	Suggested Improvements: 
<b>iv1.</b> Manual testing is not compared with WAM-SE. </br>
<b>iv2.</b> The authors refers to the fact that symbolic execution based techniques are notoriously expensive. They customize the symbolic execution to capture only constraints related to interface definitions but don’t explain how they achieve so.</br>
<b>iv3.</b> For the evaluations the authors considered only four Java based applications. For better results more number and variety of applications should have been considered.</br>
<h1>v. Connection to paper one: </h1>
The first paper was on automated web application testing using search based software engineering. This paper identifies interfaces for improving testing and analysis of web applications. In paper one the static analysis that determined the type of inputs based on the type of constants to which they are compared or from which they are assigned are similar to this paper. Although in paper one, they cannot infer types for all inputs and needs has to be augmented manually.</br>

<h1>References:</h1>
1.	F. Ricca and P. Tonella. Analysis and Testing of Web Applications. In International Conference on Software Engineering, pages 25-34, May 2001.
2.	X. Jia and H. Liu. Rigorous and Automatic Testing of Web Applications. In 6th IASTED International Conference on Software Engineering and Applications, pages 280-285, November 2002.
3.	A. A. Andrews, J. Outt, and R. T. Alexander. Testing Web Applications by Modeling with FSMs. In Software Systems and Modeling, pages 326-345, July 2005.
4.	S. Elbaum, K.-R. Chilakamarri, M. F. II, and G. Rothermel. Web Application Characterization Through Directed Requests. In International Workshop on Dynamic Analysis, pages 49-56, May 2006.
5.	Y. Huang, S. Huang, T. Lin, and C. Tsai. Web Application Security Assessment by Fault Injection and Behavior Monitoring. In Proc. of the 12th International World Wide Web Conference (WWW 03), pages 148-159, May 2003.
