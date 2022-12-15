# Tables: 

![tables](https://user-images.githubusercontent.com/113796019/204119696-cb61753d-65d0-4739-9be3-d05e5fea22a5.jpeg)

# 15 Questions (5 Use Cases each):

**1. Top 5 USA universities.**

SQL Query :  

    Select University_name from University Where Country = "USA" order by National_Rank asc limit 5;

<img width="275" alt="Query-1" src="https://user-images.githubusercontent.com/113796019/204119387-a8f00c7d-1472-4cd7-aec5-05b397094e56.png">

**2. Top 5 universities that provides best education.**

SQL Query :  
   
    select university.university_name, standards.Quality_of_Education from University left join Standards on university.university_ID = standards.university_ID order by standards.quality_of_education limit 5;

<img width="274" alt="Query-2" src="https://user-images.githubusercontent.com/113796019/204119549-a7eab990-5d18-4ce0-9b6d-42da2bf0a46a.png">

**3. Top 10 ambitious institutes.**

SQL Query :  

    Select University_ID, University_name, Chance_of_admit from university order by chance_of_Admit limit 10;

<img width="275" alt="Query-3" src="https://user-images.githubusercontent.com/113796019/204119581-f515492c-a20b-4963-b617-3fdbd9d7fc4e.png">

**4. Rate the university based on quality of faculty.**

SQL Query :  

    Select university.University_Id, university.University_name, standards.Quality_of_Faculty from University left join Standards on University.University_ID = Standards.University_ID order by Quality_of_Faculty;

<img width="345" alt="Query-4" src="https://user-images.githubusercontent.com/113796019/204119589-ab935eca-8264-4e2e-8896-f56197fe710b.png">

**5. Count the number of universities with distinct university ratings.**

SQL Query :  

    Select University_rating, Count(University_Name) as No_of_Universities from university group by University_rating order by University_rating;

<img width="176" alt="Query-5" src="https://user-images.githubusercontent.com/113796019/204119593-eaa8edbd-ba24-45d6-926e-e43f415ce499.png">

**6. universities that does not require research.**

SQL Query :  

    Select University_name from University left join requirements on University.University_ID = Requirements.University_ID where research = 0;`

<img width="219" alt="Query-6" src="https://user-images.githubusercontent.com/113796019/204119598-43dae9d9-1f33-49d7-a995-1de6ec922096.png">

**7. Universities that are best fit for a student with GRE score 315 and TOEFL score 110.**

SQL Query : 

    Select University.University_Id, University_Name, GRE, TOEFL from University left join Requirements On University.University_Id = Requirements.University_Id where GRE between 310 and 316 && TOEFL between 105 and 112;

<img width="345" alt="Query-7" src="https://user-images.githubusercontent.com/113796019/204119604-69ed08f5-1474-404b-b726-e627e33a0c19.png">

**8. Should a student with GRE score "321" apply to Northeastern University?**

SQL Query : 

    select University_name, GRE, case when GRE < 321 then 'YES' else 'NO' End as Decision From University left join requirements on University.University_ID = Requirements.University_ID where University_name = 'Northeastern University';

<img width="220" alt="Query-8" src="https://user-images.githubusercontent.com/113796019/204119607-8f5c7da1-af20-4362-9d4f-8e5755935d67.png">

**9. What are the pre requisites to apply to Northeastern University?**

SQL Query : 

    Select University.University_ID, University_name, year, score, gre, toefl, sop, lor, cgpa, research from University right join Requirements on University.University_ID = requirements.University_ID where University_name = 'Northeastern University';

<img width="451" alt="Query-9" src="https://user-images.githubusercontent.com/113796019/204119612-9d7b2c98-040c-412d-a216-74e342868f29.png">

**10. Number of students employed from university of Oklahoma.**

SQL Query : 

    Select University.University_ID, University_name, Alumni_Employement from University inner join Standards on standards.University_ID = University.University_ID where University_name = 'University of Oklahoma - Norman Campus';

<img width="370" alt="Query-10" src="https://user-images.githubusercontent.com/113796019/204119618-1232ca35-d379-473b-a277-51ab1ab26eab.png">

**11. What is the basic GPA requirement and chance of getting admit at 'University of Pennsylvania'?**

SQL Query : 

    Select University_Name, CGPA from Requirements left join University on Requirements.university_id = University.university_id where university_name = 'University of Pennsylvania';

<img width="171" alt="Query-11" src="https://user-images.githubusercontent.com/113796019/204119623-e40bd8e5-722d-47ef-907d-28c3867006a0.png">

**12. What is the university_rating and national_rank of Cornell University?**

SQL Query : 

    Select University_name, University_rating, national_rank from University where University_Name = 'Cornell University'

<img width="250" alt="Query-12" src="https://user-images.githubusercontent.com/113796019/204119627-4425ba51-76c2-46d5-ab2e-c928fb8789c7.png">

**13. Which university has highest GRE and GPA requirements?**

SQL Query : 

    Select university_name , min(CGPA) , min(GRE) from University left join Requirements on  University.university_id = Requirements.university_id;

<img width="218" alt="Query-13" src="https://user-images.githubusercontent.com/113796019/204119630-a72fbe56-8fd1-4805-918a-5d3615604d2b.png">

**14. University with highest alumni employment and publications?**

SQL Query : 

    Select university_name, max(alumni_Employement) from University left join Standards on University.university_id = Standards.university_id;

<img width="224" alt="Query-14" src="https://user-images.githubusercontent.com/113796019/204119633-9c68eb2d-e51b-4dc9-9d34-22b1ea99dfcc.png">

**15. View the university with lowest score in the year 2012.**

SQL Query : 

    Select University_name, min(score) from University left join requirements on University.University_ID = Requirements.University_ID where academic_year = '2012';

<img width="256" alt="Query-15" src="https://user-images.githubusercontent.com/113796019/204119636-bedab2c2-7f1e-4c1c-8bed-e80d54fb5533.png">





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

