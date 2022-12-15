# Previous Use Cases of each team member:

## Shreyasi

1.  What is the tuition Fees of a particular course?

    The dataset does not have a details of tuition fees.

2.  What are the admission requirements of a course?

    We have admission requirements of a particular university but since there are no course detials we cannot fetch the requirements of a specific course.
    
    SQL Query:

        Select University.university_ID, University_name, Score, GRE, TOEFL, SOP, LOR, CGPA from university right join requirements on University.university_Id = Requirements.University_ID;
        
    <img width="466" alt="shreyasi-2" src="https://user-images.githubusercontent.com/113796019/204204284-62b32fdb-fcb5-4393-8115-5ec16ff9d695.png">


3.  What is the course structure? 

    The dataset does not have a details of course structure.

4.  Which universities have waived of GRE score?

    All the universities in the dataset have specific GRE score requirement.

5.  Top universities for GRE score less than 320?

    SQL Query:

        Select University.university_ID, University_name, GRE from university right join requirements on University.university_Id = Requirements.University_ID where GRE < 320;
        
    <img width="299" alt="shreyasi-5" src="https://user-images.githubusercontent.com/113796019/204204665-ad322a17-b8b5-44dd-88be-c5471614f14a.png">

6.  What are the total number of international students registered in the university? 

    No such information present in the dataset.

7.  Number of courses available in the university? 

    The dataset does not have a details of courses.

8.  What is the course duration? 

    The dataset does not have a details of courses.

9.  What is the campus location?

    SQL Query:

        Select University_Name, Country from University;
        
    <img width="221" alt="shreyasi-9" src="https://user-images.githubusercontent.com/113796019/204204701-add56397-edbd-4b1f-8a63-e6ce2160f284.png">

10. How much is the application fees?

    Application fees details not available in the dataset


## Somesh R

1.  Search for universities which ranks between top 20-30.

    SQL Query:

        Select University_name, national_rank from University where national_rank BETWEEN 20 and 30;
        
    <img width="275" alt="Somesh-1" src="https://user-images.githubusercontent.com/113796019/204204757-2c3dcd81-f221-42d3-9a31-ca1d38be4ca9.png">

2.	View the universities which has CGPA cutoff of 3.5 and above.

    SQL Query:

        Select University.University_Id, university_name from University left join Requirements on  University.university_id = Requirements.university_id where CGPA >= 3.5;
        
    <img width="280" alt="Somesh-2" src="https://user-images.githubusercontent.com/113796019/204204789-cf5dd974-1ff9-47a8-843e-dda740103a75.png">

3.	View the universities which offer course of “Computer science and engineering”.

    The dataset does not have details of courses.

4.	View the course which has requirements of IELTS<7.0 band.

    The dataset does not have details of courses.

5.	View the twitter username for the tweets related to Princeton University.

    The dataset does not have a details of twitter scap data.

6.  Which universities have a higher acceptance rate and a lower graduation rate?

    The dataset does not have details of graduation rate.

7.  Which universities have a high intake of international students in fall 2022?

    The dataset does not have details of intake of international students.

8.  Determine which university is in a developed location and has a vast job market (city or rural).

    No such information present in the dataset.

9.  How many universities have a high graduation rate in 2021?

    The dataset does not have details of graduation rate.

10. Which universities have IVY league status and view acceptance rate?

    The dataset does not have details of IVY league status.

11.	Which universities require a minimum score of 7 bands in IELTS and TOEFL > = 100?

    The dataset does not have details of IELTS.
    
    SQL Query:

        Select University.University_Id, University_Name, GRE, TOEFL from University left join Requirements On University.University_Id = Requirements.University_Id  where TOEFL >= 100;
        
    <img width="350" alt="Somesh-3" src="https://user-images.githubusercontent.com/113796019/204204844-88d087d3-1b53-4578-806c-0a1e941e4e4c.png">

12.	Determine which universities have GRE requirements such as Verbal > = 155, Quants > = 160, and AWA > = 3.

    All the universities in the dataset have combined GRE score requirement.

13. What is the acceptance rate of students with a CGPA > = 7?

    SQL Query:

        Select University.University_Id, university_name, Chance_of_Admit from University left join requirements on University.University_ID = Requirements.University_ID where CGPA >= 7;
        
    <img width="384" alt="Somesh-4" src="https://user-images.githubusercontent.com/113796019/204204882-839177e4-b4fc-4bd9-be64-a4a9ed6eb293.png">

14. What is the most popular course of study in the top 10–20 universities?

    The dataset does not have a details of courses.

15. Which of the following private universities doesn’t have GRE or English proficiency exam requirements for application?

    All the universities in the dataset have combined GRE and IELTS/TOEFL requirement.

## Preksha

1.  What are the top 10 universities for a particular course? 

    Database does not have details of course name .

2.  What are the top 3 universities in a state? 

    Database does not have a state name.

3.  What is the acceptance rate of the university ?

    SQL Query:
    
        Select university_name, chance_of_admit from university where university_name = 'Northeastern University';
        
    <img width="203" alt="Preksha-3" src="https://user-images.githubusercontent.com/113796019/204204971-59e77a60-4866-4d79-89e3-6ca33fdc5599.png">

4.  What is the placement rate of the university ?

    SQL Query:
    
        Select university_name, alumni_employement from University left join Standards on University.university_id = Standards.university_id;
        
    <img width="263" alt="Preksha-4" src="https://user-images.githubusercontent.com/113796019/204204992-e1612cd6-def1-437b-98ac-f6f005bc20e1.png">

5.  What is the financial aid of the university? 

    Database does not have a financial  aid

6.  What are the top universities for TOEFL scores less than 100?

    SQL Query:
    
        Select university_name, TOEFL, national_rank from University left join Requirements on University.university_id = Requirements.university_id order by national_rank;
        
    <img width="270" alt="Preksha-6" src="https://user-images.githubusercontent.com/113796019/204205014-005dad47-f488-4778-9636-7e3a939d76c9.png">

7.  What is the minimum score required in GRE, TOEFL.

    SQL Query:
    
        Select university_name, min(GRE), min(TOEFL) from University left join Requirements on University.university_id = Requirements.university_id;
        
    <img width="221" alt="Preksha-7" src="https://user-images.githubusercontent.com/113796019/204205053-c5766259-b529-41d4-847e-89937ae91d1b.png">

8.  What is the average GPA required for a university?

    SQL Query:
    
        Select university_name, avg(CGPA) from  University left join Requirements on University.university_id = Requirements.university_id;
        
    <img width="179" alt="Preksha-8" src="https://user-images.githubusercontent.com/113796019/204205073-e3e55304-bc15-4f03-bf8b-3a4cf2653994.png">

9.  Are there any scholarships available for international students ? 

    Scholarship details are not included in the database.

10. What are the chances of getting an admit in the university based of the students profile?

    SQL Query:
    
        Select University_name, chance_of_admit from University left join Requirements on University.university_id = Requirements.university_id where GRE = 320 AND TOEFL = 104 AND university_name = 'Northeastern University';
        
    <img width="223" alt="Preksha-10" src="https://user-images.githubusercontent.com/113796019/204205097-3c132fc7-3ebb-4d86-9e06-4bfecf3d390b.png">

