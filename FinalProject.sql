create database finalproject;
use finalproject;

Select * from Standards;
Select * from Requirements;
Select * from University;
Select * from Student_Profile;
Select * from Audit;

drop table student_profile;
drop table requirements;
drop table standards;
drop table audit;
drop table university;


-- create view for university requirement
create view University_Requirement
as
Select university.University_ID, University_name, GRE, TOEFL, SOP, LOR, CGPA, Research 
from University inner join Requirements
on University.University_Id = Requirements.University_ID;

Select * from University_Requirement;
Drop view University_Requirement;

-- Creating views for acceptance rate based on GRE score 

Create view acceptance_GRE
as
Select University.University_ID, University_name, GRE, Chance_of_Admit 
from University inner join Requirements
on University.University_ID = Requirements.University_ID;

Select * from acceptance_GRE;
Drop view acceptance_GRE;

-- Create view employment rate
Create View employment_rate
AS
Select University.university_ID, University_name, Alumni_Employement
from University inner join Standards
on University.University_ID = Standards.University_ID;

Select * from employment_rate;
Drop view employment_rate;

====================================================

-- Creating index 
Create index university_id
on University(University_id);

-- Creating index on GRE
Create index GRE_idx
on Requirements(GRE);

-- Creating index on TOEFL
Create index toefl_idx
on Requirements(TOEFL);

-- Creating index on University_ID
Create index std_uid_idx
on Standards(University_id);

-- Creating index on Quality of Education
Create index qoe_idx
on Standards(Quality_of_education);

-- Creating index on University Name
Create index Uni_name_idx
on University(University_Name);


show index from standards;
show index from requirements;
show index from university;

====================================================


-- Tigger to enter 0 in requirements table for each entry in university
DELIMITER $$
Create trigger uni_req 
AFTER INSERT ON University FOR EACH ROW 
begin
	DECLARE ID INTEGER;
	SELECT University.University_ID into @ID from University
	where University.University_ID = NEW.University_Id;
	INSERT INTO Requirements(University_ID, Academic_Year, Score, GRE, TOEFL, SOP, LOR, CGPA, Research) VALUES (@ID, 0,0,0,0,0,0,0,0);
END $$

drop trigger uni_req;
INSERT INTO University(University_ID, University_Name, Country, Chance_of_Admit, University_Rating, National_Rank)VALUES ('402', 'test', 'test', '1000', '1000', '1000');

select * from university
where university ID = "402";

select * from requirements

====================================================

-- Create stored procedure for university requirements:

DELIMITER //

CREATE PROCEDURE U_req 
(IN U_name varchar(255))
BEGIN
	SELECT University_Name, Score, GRE, TOEFL, SOP, LOR, CGPA
FROM University INNER JOIN Requirements 
On University.University_Id = Requirements.University_Id
Where University_Name = U_name;
END; //
DELIMITER ;

Call U_req('Northeastern University');


-- EXEC U_req @U_Name = 'Northeastern University'

DROP PROCEDURE U_req;


