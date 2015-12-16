#A Review of the Recent Developments in Automated Web Application Testing
-	Arnab Saha (asaha@ncsu.edu)

##1. Abstract

Testing is among the most labor intensive tasks in web application development and also one that has a strong impact on the effectiveness and efficiency of application. For these reasons it has been one of the most active topics in the research on web application testing for several decades, resulting in many approaches and tools. This paper presents a review of some of the prominent techniques for automatic generation of test cases and optimizing other aspects of web application testing.

##2. Keywords

Web application testing; search based software engineering; automated test case generation

##3. Introduction

The web has had a significant impact on all aspects of our society, from business, education, government, entertainment sectors, industry, to our personal lives. The Internet has created new ways for the people to communicate, congregate, and share information. As our society becomes more and more reliant on the web, the dependability of the web applications is becoming very important. In order to do this, many researchers have proposed various techniques to automate the testing process of web applications in the past decade. This paper talks about the various techniques which has made a significant stride in the area of web application testing.


The web can be defined as an open source information space where documents and other web resources are identified by URLs, interlinked by hypertext links, and can be accessed via the Internet. There are some reasons why this has become so increasingly popular in this era which include 1. No installation costs, 2. Upgrading with new features can be done automatically for all users, 3. Independent of the client’s operating system, 4. Universal access from any device connected to the internet, and 5. Continual availability.


There are a lot of difficulties in web application testing. Firstly the web applications are developed using different programming languages like HTML, CSS, JavaScript on the client-side and PHP, Ruby or Java on the server-side. Secondly the web applications are distributed through a client/server architecture with asynchronous HTTP request/response calls to synchronize the application state. Finally the web applications have a dynamic in nature and they possess nondeterministic characteristics.


In this paper we have reviewed a wide variety of papers from the last decade related to web applications testing which involves several aspects of search based software engineering which are getting integrated in the different testing phases. Using the help of optimization techniques and evolutionary algorithms, researchers are able to detect flaws and discrepancies in the web applications. In some of the papers they have used these techniques for effective generation of test data. In the end we have reviewed a couple of review papers on web applications testing to get an overview of the current direction of the work.


##4. Motivation 	

Despite a lot of advantages of web applications and technologies on our lives, the use of the server and browser technologies has made the web applications error-prone and challenging to the test, causing serious dependability threats [9]. Another reason is that web technologies change frequently and their adopters seek early acquisition of market share. This pressure on development time squeezes the testing phase, especially when it is not automated, labor intensive and therefore slow [1]. 


However inadequate testing poses significant risks. For example some studies has shown that online customers has impulsive purchasing habits therefore an e-commerce store can lose a lot of money if there is significant amoun¬t of downtime. With the help of the automation in web application testing, these risks can be reduced at much lesser costs.


##5. Survey results 

In this paper we have studied a range of papers related to different aspects of web applications testing in the last decade. Here we have tried to provide a brief overview of the papers and how they are relevant in automating some aspects of testing. We have divided the papers into three categories:
* Application testing techniques
* Test case generation
* Surveys on web application testing


Each of these categories is described below with some papers relevant to it. 


###5.1. Application testing techniques
Two application testing papers are studied which are described below.

####5.1.1. Automated Web Application Testing Using Search Based Software Engineering

####Overview:

This paper introduces three related algorithms and a tool, SWAT, for automated web application testing using Search Based Software Testing (SBST).


#####Keywords:
* **SBST:** Search-Based Software Testing [2] is used to automate or partially automate a testing task using meta-heuristic optimizing search technique.
* **Automated Test data generation:** A system that generates test data for a program automatically.
* **SWAT:** Search based Web Application Tester [1] is the tool used for SBST. It is composed of a Pre-processing unit, Search Based Tester and the Test Harness.
* **DMV:** Dynamically Mined Value is used to seed values in the inputs dynamically during execution.


#####Motivational statements: 

This paper introduces three related algorithms and a tool, SWAT, for automated web application testing using Search Based Software Testing (SBST). The algorithms significantly enhance the efficiency and effectiveness of traditional search based techniques exploiting both static and dynamic analysis. The combined approach yields a 54% increase in branch coverage and a 30% reduction in test effort. Each improvement is separately evaluated in an empirical study on 6 real world web applications.

#####Related Work: 

The authors mention in the paper that though SBSE has been popular for a long time, search based data generation was not applied for web applications. Marchetto and Tonella used a Hill Climbing algorithm for testing Ajax web applications. They have adopted the Alternating Variable Method (AVM) introduced by Korel [3]. The branch ordering technique is inspired from Michael et al. [4]. Levenshtein distance to calculate the fitness of strings was used from Alshraideh and Bottaci [5]. Other than that Artzi et al. [6] generated test cases for dynamic web applications automatically though the approach was different as it focused on statement coverage instead of branch coverage as in this paper. This paper uses bypass testing to bypass the interface to generate data for the server side code which was introduced by Offut et al. [7].
#####Informative visualizations: 
<img src = "../hw/read/1/visual 1 main table.png"> <br>
The total evaluation is summed up in one table. The authors implemented three versions of the tool:
<ol>
    <li>Near Miss Seeding (NMS)</li>
    <li>Static Constant Seeding (SCS) with NMS</li>
    <li>Dynamically Mined Value (DMV) with SCS</li>
</ol>
Then empirical evidence is collected how enhancements affect branch coverage, efficiency and fault finding ability.

#####Future Works: 

The system is currently semi-automated but the aim should be to produce a fully-automated product. Though major parts of the algorithm works independently, deciding input types and username/password needs to provided by the user. We also find that the algorithm doesn’t show usual characteristics in the case of Timeclock application. The author states that the behavior is due to the high precision in float constants which are mined from the application. The algorithm can be improved to handle all data types.  


####5.1.2. Precise Interface Identification to Improve Testing and Analysis of Web Applications. In ISSTA ’09, pages 285–296, 2009

#####Overview: 

The current techniques for identifying web application interfaces can be incomplete or imprecise, which hinders the effectiveness of quality assurance techniques. To address these limitations, this paper presents a new approach for identifying web application interfaces that is based on a specialized form of symbolic execution. It shows that the set of interfaces identified by their approach is more accurate than those identified by other approaches. It also shows that this increased accuracy leads to improvements in several important quality assurance techniques for web applications: test-input generation, penetration testing, and invocation verification.


#####Keywords:

* **Interface identification:** The interface execution is dependent on the input parameters and the flow of execution therefore varies at runtime for web based applications.
* **Symbolic execution:** A program operates on symbolic inputs that can represent arbitrary values and at any point in the execution variables dependent on the input are represented as algebraic expressions over the symbolic input values. 
* **ii3. Path Condition (PC):** PC expresses constraints on the symbolic inputs that must be satisfied in order for execution to reach a specific point in the program.
* **ii4. Web crawling:** It is a common approach to identify accepted interfaces. In this approach, a program called the web spider visits and analyses web pages to discover links to other pages till there are no new links to visit. This information is used to infer interface information about the individual components.


#####Motivational statements: 

The components of a dynamic web application communicate extensively via their interfaces to generate the dynamic content. In web applications these interfaces are not implicitly defined and vary at runtime. Automated quality assurance is necessary for ensuring quality in these applications.

#####Related Work: 

Many approached to interface identification has been made. Most of them rely on developer provided interface specifications. Ricca and Tonella uses developer-provided UML models [1], Jian and Liu use a formal specification [2], and Andrews, Offutt, and Alexander [3] use finite state machines. An approach by Elbaum and colleagues [4] uses a series of requests to an application to identify its interfaces and infer constraints on the IPs of the interfaces by analyzing responses to the request. A spider by Huang and colleagues [5] uses sophisticated heuristics to more effectively and thoroughly explore a web app. lication.

#####Informative visualizations: 
<img src = "../hw/read/4/1. analysis time.png"> </br>
This table shows the result of the timing experiments. For each application, the table shows the time in seconds to analyze the web application (Total Time).</br>
<img src = "../hw/read/4/2. precision.png"> </br>
This table shows the comparison of wam-se and wam-df. For each application (Subject) we list the number of interfaces identified and, in parenthesis for the wam-df approach, the additional amount of identified interfaces as compared to wam-se.</br>

#####Delivery Tools: 

The authors has developed a tool in Java called WAM-SE (Web Application Modeling with Symbolic Execution) to evaluate their approach. It consists of three modules:
* **Transform-** is used to implement the symbolic transformation. The input to this module is the bytecode of the web application and the specification of program entities to be considered symbolic (in this case, symbolic strings).
* **SE Engine-** implements the symbolic execution. The input to this module is the bytecode of the transformed web application, and the output is the set of all PCs and corresponding symbolic states for each component in the application.
* **PC Analysis-** implements the analysis. The input to this module is the set of PCs and symbolic states for each component in the application, and the output is the set of IDCs and accepted interfaces. The module iterates over every PC and symbolic state, identies the accepted interfaces, and associates the constraints on each IP with its corresponding accepted interface.


###5.2. Test case generation:

####5.2.1. Automatic string test data generation for detecting domain errors. 

#####Overview:

This paper presents a novel approach for the automatic generation of ON–OFF test points for string predicate borders, and describes a corresponding test data generator. The empirical work is conducted on a set of programs with string predicates, where extensive trials have been done for each string predicate, and the results are analyzed using the SPSS tool. 

#####Keywords: 

* **Domain Testing:** Domain testing is a software testing technique in which selecting a small number of test cases from (usually a nearly infinite) group of test cases. This is used for testing software.
* **Dynamic Test data generation:** Generation of the test data on the go where the generator intelligently modifies the test data.
* **ON-OFF test points:** ON test point lies on the given solution predicate border whereas the OFF test point lies just outside the border. They both are as close as possible to check the border points.
* **String predicate:** In this paper the string predicate border is tested on.


#####Motivational Statements: 

A lot of work on domain testing is getting generated to guarantee software quality and reliability. The most expensive step in the testing is test case generation and effective test cases determine the reliability of the software. Manually developing the test data set is expensive, laborious, difficult and error prone. So the paper is based on automatic generation of test data.

#####Related Work: 

The earlier studies which have used ON-OFF test generation has focused only on numeric types and ignored string data. The studies which addressed string test generation used string mutation operators like insertion, deletion and substitution. This study specifically addressed the problem of ON-OFF test data generation on string predicates.


#####Future Works: 

The system is currently semi-automated but the aim should be to produce a fully-automated product. If the test string in the predicate is a literal that contains one character then for predicate Max-pre1, the conclusions get invalid. These are the areas where development can be done.

####5.2.2. Finding bugs in web applications using dynamic test generation and explicit state model checking.

#####Overview: 

This technique generates tests automatically, runs the tests capturing logical constraints on inputs, and minimizes the conditions on the inputs to failing tests so that the resulting bug reports are small and useful in finding and fixing the underlying faults. The tool Apollo implements the technique for the PHP programming language. Apollo generates test inputs for a Web application, monitors the application for crashes, and validates that the output conforms to the HTML specification. This paper presents Apollo’s algorithms and implementation, and an experimental evaluation that revealed 673 faults in six PHP Web applications.

#####Keywords:

* **Web application:** These are those types of software based applications which run on a web browser. They are originally written in scripting languages and their control does not flow via simply the code but via the generated HTML text.
* **Failures in HTML:** When a problem in HTML is generated this type of error occurs. 
* **Explicit-state model checking:** It is that type of algorithm that reaches only a single level deep in the application. That means it is an algorithm that always starts the checking again from the same initial state and removes the state reached at the end of each execution. 
* **Static analysis:** It is the type of debugging technique which is done before the execution of program. It helps to provide a better understanding of the code. 


#####Motivational Statements: 

The goal of this paper is to provide a solution for avoiding problems caused by malformed web pages and web script crashes. It does this by using dynamic test generation technique. This is an automated technique which generates input and runs the code, then varies the input to obtain a bug report. 

#####Tools used: 

The prime tool used in the above mentioned test is Apollo. The first step taken by it is to execute the web application with an empty input under test. It records the dependence of control flow on input after each execution. It determines the type of failures that occur, i.e. whether the failures are execution failures or HTML failures. 

#####Tutorials: 

This paper teaches a lot of things. It shows there are two types of errors which could occur in a web application, namely HTML error and execution error. The examples mentioned are in a very organized format in a step by step way for readers with little knowledge on the subject to understand easily. 

#####Final results: 

The tool used in the test obtains a detailed report of the bug or errors which is very beneficial for readers and other researchers. The presence of accurate data and real time examples makes Apollo understandable.


####5.2.3. Automatic generation of valid and invalid test data for string validation routines using web searches and regular expressions

#####Keywords:

* **Test Effectiveness:** Ratio between coverage percentages and number of test suits determine the effectiveness of tests.
* **ii2. Generation of string data:** The paper presents a new approach to generate string test data. The technique uses program identifiers to construct web search queries for regular expressions that validate the format of a string type (such as an email address).
* **iii3. Tokenisation:** A process of dividing a stream of texts into smaller elements known as tokens.
* **iii4. Routine validation:** A program that accepts a value as an input and returns true if it is accepted and false if it is rejected.


#####Baseline Results: 

The paper presents the results of an empirical study evaluating our approach [1]. The study was conducted on 24 string input validation routines collected from 10 open source projects. While dynamic symbolic execution and search-based testing approaches were only able to generate a very low number of values successfully, our approach generated values with an accuracy of 34% on average for the case of valid strings, and 99% on average for the case of invalid strings.


#####Motivational Statements: 

There has been much work in the literature of late devoted to automated test input generation [4], however handling string input types remains a challenging task [5, 6]. This is due to the inherent complexity of real - world data that is naturally encoded as strings — e.g., dates of different formats, banking codes, registration numbers, etc. — which have very large input domains, and consequently, involve a huge search space for test data generation. In the paper web searches are made for strings that match the regular expressions, producing examples of test cases that are both valid and realistic. Following this, our technique mutates the regular expressions to drive the search for invalid strings, and the production of test inputs that should be rejected by the validation routine.

#####Related work: 

The input validation problem has been addressed in the classic software testing literature [2]. The earlier approaches assume the provision of grammars from which the inputs can be generated. Beizer [2] has presented approaches for syntax testing, also called grammar-based testing, where the syntax of the input is expressed in a formal specification, such as BNF and its equivalent graph. Then the valid inputs are generated by “covering” the graph. Invalid values can also be generated by employing heuristics such as interchanging terminal and non-terminal symbols (in the BNF), replacing numeric with alphabetic values and generating extra delimiters in the valid values — the so-called “error-condition” rules[3].

###5.3. Surveys on web application testing

####5.3.1. SBSE for software product line engineering: a survey and directions for future work

#####Keywords:

* **SPL:** A Software product line is a collection of similar products of where all share some core functionality, where each differs in some specific features [10].
* **SBSE:** SBSE is a process of using computation search as a technique to optimize software engineering problems. 
* **Program Synthesis:** The task of autonomously discovering an executable piece of code using various constraints such as input-output examples.
* **Genetic Programming:** It is an algorithm inspired by biological evolution to find computer codes that perform a user defined task.


#####Motivational statements: 

Feature model plays a critical role in capturing and expressing relationships between the requirements for products.

#####Best Practices: 

Product line architecture is used to control the core features, shared by all products present on the product line.

#####Future Work: 

There are some possibilities for new avenues of work in which the community might apply computational search to software product line engineering. They are namely auto growing new SPL product branches, auto merging to tackle branch mania and retargeting existing SBSE at SPL.

#####Related work: 

The term \'Search Based Software Engineering\', coined in 2001 [1], refers to the use of computational search as a means of optimising software engineering problems. Since 2001, SBSE has been used to address challenging software engineering problems with large and complex search spaces, characterised by many conflicting competing objectives, in areas as diverse as requirements [4], predictive modelling [2, 3] software project management [5], design [6], testing [7], refactoring [8] and repair [9]. This wide applicability to problems characterised by similar features to those found in SPL engineering, naturally suggests that SBSE will find successful applications in SPL optimisation. This observation has led to a recent upsurge in interest and activity in the area of `SBSE for SPL'.


####5.3.1. A systematic literature review, Journal of Systems and Software

#####Keywords:

* **SLR:** Systematic Literature Review is to identify, analyze and classify the state-of-the-art research papers and provide an overview of the trends in a specific field.
* **WAT:** Web Application testing is necessary as our society relies more and more on the web and the dependability of web applications has become increasingly important.
* **SM:** This study is a follow up and complimentary study to a Systematic Mapping which was conducted in the area.
* **RQs of the study:** Three research questions are explored in the studies which are related to define selection and exclusion criteria, and synthesize the empirical evidence in this area.

#####Motivational statements: 

The web has had a significant impact on all aspects of our society. As our society relies more and more on the web, the dependability of web applications has become increasingly important. To make these applications more dependable, for the past decade researchers have proposed various techniques for testing web-based software applications. This literature search for related studies retrieved 193 papers in the area of web application testing, which have appeared between 2000 and 2013. As this research area matures and the number of related papers increases, it is important to systematically identify, analyze, and classify the publications and provide an overview of the trends and empirical evidence in this specialized field. [2]

#####Related Work: 

The authors explain that this study is an extension of the Systematic Mapping study [1]. The paper classifies the related works in three categories: (1) secondary studies that have been reported in the broader area of software testing, (2) online repositories in software engineering, and (3) secondary studies focusing on web application testing. The studies are shown in the table below.
  
#####Patterns and anti-patterns: 

The authors included 95 of the initial 193 papers in this study. They synthesized the following data/findings from the papers: (1) the types of input/inferred test models, (2) the fault models/bug taxonomy related to web applications, (3) test tools proposed in this area and their capabilities, (4) metrics used for assessing cost and effectiveness of WAT techniques, (5) the threats to validity in the empirical studies, (6) level of rigor and industrial relevance of the empirical studies, and (7) evidence regarding the scalability of the WAT techniques. In answering RQ 1.2, they have extracted the types of fault models/bug taxonomies specific to web applications. They also found that over 50 types of faults have been discussed. Test techniques targeting some of these fault types have been proposed. It is worth conducting more in-depth studies in future to ensure coverage of all the fault types by the test techniques and also the effectiveness of those techniques on detecting each specific fault type.
