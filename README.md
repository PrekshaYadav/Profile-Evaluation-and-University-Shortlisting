# Project Report for Info 16149 - Data Management and Data Design


## Topic Name:  
Profile Evaluation and University Shortlisting
<br />

## Group members :

Preksha Chandrashekhar Yadav - 002787954

Shreyasi Wakankar - 002771284

Somesh Ramakanth Ramisetty - 002776372

## Overview 

Being international students we are aware of the problem faced by the students while shortlisting and finalizing the University and hence in this project we’ll be creating a set of databases which will have a list of at least 100 universities along with the prerequisites of each course. 

The main focus of the project is to evaluate a student's profile and thereby shortlist the universities on the basis of their portfolio. We will be retrieving the data by scrapping various websites and combining the cleaned data to create a proper database for the accurate prediction of acceptance and recommendation of the Universities.

To fetch the data we’ll be scraping the data from US news, YMgrad and Yocket. After cleaning the fetched  data the variables that will be used are - University Name, City/State, Ranking, Programs, Fees, Prerequisites, Acceptance Rate, Application fee waiver etc. Thereafter predicting the chances of acceptance and recommending universities  by using database queries and  regression techniques.

The Key feature of the project is that instead of referring to multiple websites which only have data of their subscribed students, one can find a perfect solution on this database. Since we are merging various databases, the recommendations will be accurate. 



## Steps to be followed:
1. Clone the project
2. Create a database - CREATE DATABASE FinalProject
3. Execute MainExecutionFile.py: this file will execute the below files
    1. Connector.py
    2. Importing_Dataset.py
    3. YMGrad_Scraper.py
    4. Visualization.py
    5. Prediction_model.py
4. Execute commands from finalproject.sql to create views, indexes, triggers and procedures
5. Execute studentlogin.sql to create Logindetails and Student table
6. Execute the following command in the terminal
    python./app.py
7. In the retrieved output click on "http://localhost:8080"
8. Register in the website using your email id
9. Log into the page 
10. Filter the universities based on your profile by giving GRE Score, TOEFL Score and CGPA
11. You can also search the university by giving the university name in the search box.
12. To take the backup of the database from MySQL:
    1. Click on server > database export
    2. Change the name of the backup
    3. Click on start export
13. To import the database in MySQL:
    1. Click on server > database import
    2. Select the path path where you created the backup
    3. Click on start import



## Documentation files:
1. Summary.md - this file has the summary of this entire project and the screenshots of all the outputs
2. Diagram.md - this file has ER diagram and UML diagram to get a better understanding of the project
3. Usecases.md - this file has the use cases and the screenshots of their output
