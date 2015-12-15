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
#####Keywords:
ii1. SBST: Search-Based Software Testing [2] is used to automate or partially automate a testing task using meta-heuristic optimizing search technique.
ii2. Automated Test data generation: A system that generates test data for a program automatically.
ii3. SWAT: Search based Web Application Tester [1] is the tool used for SBST. It is composed of a Pre-processing unit, Search Based Tester and the Test Harness.
ii4. DMV: Dynamically Mined Value is used to seed values in the inputs dynamically during execution.

ii.	Brief Notes:
iii1. Motivational statements: Successful web applications get modified each day to adopt the needs of its users but due to time and labor constraints they are often not tested properly. Now due to inadequate testing, applications face a lot of risk such as increased down time and potential loss of customers and money. Therefore a lot of research is being made to automate the testing phase by using Search based testing.
iii2. Related Work: The authors mention in the paper that though SBSE has been popular for a long time, search based data generation was not applied for web applications. Marchetto and Tonella used a Hill Climbing algorithm for testing Ajax web applications. They have adopted the Alternating Variable Method (AVM) introduced by Korel [3]. The branch ordering technique is inspired from Michael et al. [4]. Levenshtein distance to calculate the fitness of strings was used from Alshraideh and Bottaci [5]. Other than that Artzi et al. [6] generated test cases for dynamic web applications automatically though the approach was different as it focused on statement coverage instead of branch coverage as in this paper. This paper uses bypass testing to bypass the interface to generate data for the server side code which was introduced by Offut et al. [7].
iii3. Informative visualizations: 
iii4. Future Works: The system is currently semi-automated but the aim should be to produce a fully-automated product. Though major parts of the algorithm works independently, deciding input types and username/password needs to provided by the user. We also find that the algorithm doesn’t show usual characteristics in the case of Timeclock application. The author states that the behavior is due to the high precision in float constants which are mined from the application. The algorithm can be improved to handle all data types.  
