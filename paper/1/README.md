<h3>i.	Reference to the paper:</h3> 
<b>Nadia Alshahwan and Mark Harman. 2011. Automated Web Application Testing Using Search Based Software Engineering. In Proceedings of the 26th IEEE/ACM International Conference on Automated Software Engineering</b>

<h3>ii.	Most important keywords:</h3> 
<h4>ii1. SBST:</h4> Search-Based Software Testing [2] is used to automate or partially automate a testing task using meta-heuristic optimizing search technique.
<h4>ii2. Automated Test data generation:</h4> A system that generates test data for a program automatically.
<h4>ii3. SWAT:</h4> Search based Web Application Tester [1] is the tool used for SBST. It is composed of a Pre-processing unit, Search Based Tester and the Test Harness.
<h4>ii4. DMV:</h4> Dynamically Mined Value is used to seed values in the inputs dynamically during execution.

<h3>iii. Brief Notes:</h3> 
<h4>iii1. Motivational statements:</h4> Successful web applications get modified each day to adopt the needs of its users but due to time and labor constraints they are often not tested properly. Now due to inadequate testing, applications face a lot of risk such as increased down time and potential loss of customers and money. Therefore a lot of research is being made to automate the testing phase by using Search based testing to make testing less reliant on slow laborous process [1].
<h4>iii2. Related Work:</h4> The authors mention in the paper that though SBSE has been popular for a long time, search based data generation was not applied for web applications. Marchetto and Tonella used a Hill Climbing algorithm for testing Ajax web applications. They have adopted the Alternating Variable Method (AVM) introduced by Korel [3]. The branch ordering technique is inspired from Michael et al. [4]. Levenshtein distance to calculate the fitness of strings was used from Alshraideh and Bottaci [5]. Other than that Artzi et al. [6] generated test cases for dynamic web applications automatically though the approach was different as it focused on statement coverage instead of branch coverage as in this paper. This paper uses bypass testing to bypass the interface to generate data for the server side code which was introduced by Offut et al. [7].
<h4>iii3. Informative visualizations:</h4>
<h4>iii4. Future Works:</h4> The system is currently semi-automated but the aim should be to produce a fully-automated product. Though major parts of the algorithm works independently, deciding input types and username/password needs to provided by the user. We also find that the algorithm doesn’t show usual characteristics in the case of Timeclock application. The author states that the behavior is due to the high precision in float constants which are mined from the application. The algorithm can be improved to handle all data types. 

<h3>iv. Suggested Improvements:</h3>
<b>iv1.</b> As the algorithm cannot generate the input types by itself this procedure is yet to become fully autonomous. Learning algorithms can be used to automate this part. 
<b>iv2.</b> Also we find that the algorithms struggles with handling float constants which led to increased effort in the subsequent algorithms. Better techniques to handle float constants and similar data types can be generated.
<b>iv3.</b> In the cases where improvements were not shown with the subsequent algorithms, the authors provided with an intuitive explanation without any proofs. Similar algorithms can be tested to confirm if they show the same characteristics. Only then one can conclude the correct reason of the strange behavior.


<h3> References:</h3> 
<ol>
    [<li>]Nadia Alshahwan and Mark Harman. 2011. Automated Web Application Testing Using Search Based Software Engineering. In Proceedings of the 26th IEEE/ACM International Conference on Automated Software Engineering</li>
    <li>McMinn, P., "Search-Based Software Testing: Past, Present and Future," in Software Testing, Verification and Validation Workshops (ICSTW), 2011 IEEE Fourth International Conference on , vol., no., pp.153-163, 21-25 March 2011 doi: 10.1109/ICSTW.2011.100</li>
    <li>B. Korel. Automated software test data generation. IEEE Transactions on Software Engineering, 16(8):870–879, 1990.</li>
    <li>C. C. Michael, G. McGraw, and M. A. Schatz. Generating software test data by evolution. IEEE Transactions on Software Engineering, 27:1085–1110, 2001.</li>
    <li>Mohammad Alshraideh and Leonardo Bottaci. Search-based software test data generation for string data using program-specific search operators. Software Testing, Verification and Reliability, 16(3):175–203, 2006.</li>
    <li>Shay Artzi, Adam Kiezun, Julian Dolby, Frank Tip, Daniel Dig, Amit Paradkar, and Michael D. Ernst. Finding bugs in web applications using dynamic test generation and explicit-state model checking. IEEE Transactions on Software Engineering, 36:474–494, 2010.</li>
    <li>Jeff Offutt, Ye Wu, Xiaochen Du, and Hong Huang. Bypass testing of web applications. ISSRE ’04, pages 187–197, 2004.
</ol>