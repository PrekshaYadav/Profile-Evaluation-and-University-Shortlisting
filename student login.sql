use finalproject;
SELECT * FROM university;
select * from requirements;
select * from standards;
select u.University_ID, u.University_Name, u.University_Rating, u.National_Rank, u.Tuition_Fees, s.Quality_of_Education, s.Quality_of_Faculty, s.Alumni_Employement from university u join requirements r on u.University_ID=r.University_ID join standards s on s.University_ID=u.University_ID where (r.GRE between 300-3 and 300+3) and (r.TOEFL between 100-3 and 100+3) and (r.CGPA between 9-0.5 and 9+0.5);



drop procedure if exists shortlist;
delimiter $$
create procedure shortlist(gre_in int, toefl_in int, cgpa_in float)
begin
	select u.University_Name University, u.University_Rating Rating, u.National_Rank "Rank", u.Tuition_Fees Tuition, s.Quality_of_Education EducationQuality, s.Alumni_Employement Placements from university u join requirements r on u.University_ID=r.University_ID join standards s on s.University_ID=u.University_ID where (r.GRE between gre_in-3 and gre_in+3) and (r.TOEFL between toefl_in-3 and toefl_in+3) and (r.CGPA between cgpa_in-0.5 and cgpa_in+0.5);
end$$
delimiter ;



call shortlist(300, 100, 9);


DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(128) NOT NULL,
  `last_name` varchar(128) NOT NULL,
  `full_name` varchar(256) GENERATED ALWAYS AS (concat_ws(_utf8mb4' ',`first_name`,`last_name`)) VIRTUAL,
  `address` varchar(300) NOT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `email_address` varchar(500) NOT NULL,
  PRIMARY KEY (`email_address`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `phone` (`phone`)
);


DROP TABLE IF EXISTS `loginDetails`;
CREATE TABLE `loginDetails` (
  `email_address` varchar(500) NOT NULL,
  `pass` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`email_address`),
  CONSTRAINT `login_fk_student` FOREIGN KEY (`email_address`) REFERENCES `student` (`email_address`) ON DELETE CASCADE ON UPDATE CASCADE
);


drop procedure if exists create_user;
delimiter $$
create procedure create_user(in first varchar(500),in last varchar(500),in address varchar(500),in ph varchar(15), in em varchar(300), in  passcode varchar(15))
begin
	declare temp1 varchar(500);
    declare temp2 varchar(500);
	select email_address into temp1 from loginDetails where email_address=em;
    select email_address into temp2 from student where email_address=em;
    
	if temp1<=>null and  temp2<=>null then
		
		insert into student(first_name,last_name,address,phone,email_address) values(first,last,address,ph,em);
        insert into loginDetails(email_address,pass) values(em,passcode);
        if exists(select email_address from loginDetails) then
			select 1 response;
		else
			select 0 response;
		end if;
	else
		select 0 response;
	end if;
end $$
delimiter ;

call create_user("test","l","address","2121121","test@gmail.com","test@123");


drop procedure if exists check_user;
delimiter $$
create procedure check_user(in email varchar(500),in pw varchar(255))

begin
	declare t varchar(500) default null;
	select pass into t   from loginDetails where email_address=email ;
    if (select pass from loginDetails where email_address=email) <=> pw then
		select "yes" response;
	else 
		select "no" response;
	end if;
    
end $$
delimiter ;
