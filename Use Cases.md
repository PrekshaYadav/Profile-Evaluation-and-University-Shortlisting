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

