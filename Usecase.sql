Use assignment3;

Select * from Standards;
Select * from Requirements;
Select * from University;

1. Top 5 USA universities.
Select University_name from University
Where Country = "USA" 
order by National_Rank asc
limit 5;

2. Top 5 uni that provides best education.
select university.university_name, standards.Quality_of_Education
from University left join Standards
on university.university_ID = standards.university_ID
order by standards.quality_of_education
limit 5;

3. Top 10 ambitious institutes.
Select University_ID, University_name, Chance_of_admit from university
order by chance_of_Admit 
limit 10;

4. Rate the university based of quality of faculty.
Select university.University_Id, university.University_name, standards.Quality_of_Faculty 
from University left join Standards
on University.University_ID = Standards.University_ID
order by Quality_of_Faculty;

5. Count the no of uni with distinct uni ratings.
Select University_rating, Count(University_Name) as No_of_Universities 
from university
group by University_rating
order by University_rating;

6. Univ that does not require research
Select University_name 
from University left join requirements
on University.University_ID = Requirements.University_ID
where research = 0;

7. Univs that are best fit for a student with GRE score 315 and TOEFL score 110.
Select University.University_Id, University_Name, GRE, TOEFL 
from University left join Requirements
On University.University_Id = Requirements.University_Id
where GRE between 310 and 316 && TOEFL between 105 and 112;

8. Should a student with GRE score "321" apply to Northeastern University 
select University_name, GRE,
case 
when GRE < 321 then 'YES'
else 'NO'
End as Decision
From University left join requirements
on University.University_ID = Requirements.University_ID
where University_name = 'Northeastern University';

9. What are the pre requisites to apply to NEU
Select University.University_ID, University_name, academic_year, score, gre, toefl, sop, lor, cgpa, research
from University right join Requirements
on University.University_ID = requirements.University_ID
where University_name = 'Northeastern University';

10. Number of students employed from university of Oklahoma
Select University.University_ID, University_name, Alumni_Employement
from University inner join Standards
on standards.University_ID = University.University_ID
where University_name = 'University of Oklahoma - Norman Campus'

11. What is the basic GPA requirement and chance of getting admit at 'University of Pennsylvania'?
Select University_Name, CGPA from Requirements left join University 
on Requirements.university_id = University.university_id 
where university_name = 'University of Pennsylvania';


12.	What is the university_rating and national_rank of Cornell University?
Select University_name, University_rating, national_rank
from University
where University_Name = 'Cornell University'

13.	Which university has highest GRE and GPA requirements?
Select university_name , min(CGPA) , min(GRE) from University left join Requirements 
on  University.university_id = Requirements.university_id ;

14.	University with highest alumni employment and publications?
Select university_name, max(alumni_Employement) from University left join Standards 
on University.university_id = Standards.university_id;

15.	View the university with lowest score in the year 2012.
Select University_name, min(score) from University left join requirements
on University.University_ID = Requirements.University_ID
where academic_year = '2012'

Previous use cases:
-----Shreyasi-----
1. What is the tuition Fees of a particular course?
The dataset does not have a details of tuition fees.

2. What are the admission requirements of a course?
We have admission requirements of a particular university but since there are no course detials we cannot fetch the requirements os a specific course

Select University.university_ID, University_name, Score, GRE, TOEFL, SOP, LOR, CGPA
from university right join requirements
on University.university_Id = Requirements.University_ID

3. What is the course structure? 
The dataset does not have a details of course structure.

4.Which universities have waived of GRE score?
All the universities in the dataset have specific GRE score requirement

5.Top universities for GRE score less than 320? 
Select University.university_ID, University_name, GRE
from university right join requirements
on University.university_Id = Requirements.University_ID
where GRE < 320

6. What are the total number of international students registered in the university? 
No such information present in the dataset

7. Number of courses available in the university? 
The dataset does not have a details of courses.

8. What is the course duration? 
The dataset does not have a details of courses.

9. What is the campus location? 
Select University_Name, Country
from University

10. How much is the application fees?
Application fees details not availablein the dataset



------Preksha------


1. What are the top 10 universities for a particular course? 
Database does not have details of course name .

2. What are the top 3 universities in a state? 
Database does not have a state name.

3. What is the acceptance rate of the university ? 
Select university_name, chance_of_admit from university 
where university_name = 'Northeastern University';

4. What is the placement rate of the university ? 
Select university_name, alumni_employement from University left join Standards 
on University.university_id = Standards.university_id;

5.What is the financial aid of the university? 
Database does not have a financial  aid

6.What are the top universities for TOEFL scores less than 100? 
Select university_name, TOEFL, national_rank from University left join Requirements 
on University.university_id = Requirements.university_id order by national_rank;

7.What is the minimum score required in GRE, TOEFL . 
Select university_name, min(GRE), min(TOEFL) from University left join Requirements 
on University.university_id = Requirements.university_id;

8.What is the average GPA required for a university? 
Select university_name, avg(CGPA) from  University left join Requirements 
on University.university_id = Requirements.university_id;

9.Are there any scholarships available for international students ? 
Scholarship details are not included in the database.

10.What are the chances of getting an admit in the university based of the students profile? 
Select University_name, chance_of_admit from University left join Requirements 
on University.university_id = Requirements.university_id 
where GRE = 320 AND TOEFL = 104 AND university_name = 'Northeastern University';



--------Somesh--------


1.Search for universities which ranks between top 20-30.
Select University_name, national_rank from University 
where national_rank BETWEEN 20 and 30;

2.View the universities which has CGPA cutoff of 3.5 and above.
Select University.University_Id, university_name from University left join Requirements 
on  University.university_id = Requirements.university_id
where CGPA >= 3.5;

3.View the universities which offer course of “Computer science and engineering”.
The dataset does not have details of courses.

4.View the course which has requirements of IELTS<7.0 band.
The dataset does not have details of courses.

5.View the twitter username for the tweets related to Princeton University.
The dataset does not have a details of twitter scap data.

6.Which universities have a higher acceptance rate and a lower graduation rate?
The dataset does not have details of graduation rate.

7.Which universities have a high intake of international students in fall 2022?
The dataset does not have details of intake of international students.

8.Determine which university is in a developed location and has a vast job market (city or rural).
No such information present in the dataset.

9.How many universities have a high graduation rate in 2021?
The dataset does not have details of graduation rate.

10.Which universities have IVY league status and view acceptance rate?
	The dataset does not have details of IVY league status.

11.Which universities require a minimum score of 7 bands in IELTS and TOEFL > = 100?
The dataset does not have details of IELTS.
Select University.University_Id, University_Name, GRE, TOEFL 
from University left join Requirements On University.University_Id = Requirements.University_Id 
where TOEFL >= 100;

12.Determine which universities have GRE requirements such as Verbal > = 155, Quants > = 160, and AWA > = 3.
All the universities in the dataset have combined GRE score requirement.

13.What is the acceptance rate of students with a CGPA > = 7?
Select University.University_Id, university_name, Chance_of_Admit 
from University left join requirements 
on University.University_ID = Requirements.University_ID where CGPA >= 7;

14.What is the most popular course of study in the top 10–20 universities?
The dataset does not have a details of courses.

15.Which of the following private universities doesn’t have GRE or English proficiency exam requirements for application?
All the universities in the dataset have combined GRE and IELTS/TOEFL requirement.
