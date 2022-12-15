import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Sh_reyasi03")
mycursor = mydb.cursor()

mycursor.execute("Use finalproject")

print("start")
#Create table commands
mycursor.execute("Create Table University(University_ID int NOT NULL, University_Name VARCHAR(255), Country VARCHAR(255), Chance_of_Admit numeric(9,2), University_Rating int, National_Rank int, Tuition_Fees int, PRIMARY KEY (University_ID))")
mycursor.execute("Create Table Standards(Standards_ID int Not NULL AUTO_INCREMENT, University_ID int NOT NULL, Quality_of_Education int NOT NULL, Quality_of_Faculty int, Alumni_Employement int, Patent int, FOREIGN KEY (University_ID) REFERENCES University(University_ID), PRIMARY KEY(Standards_ID))")
mycursor.execute("Create Table Requirements(Requirements_ID int Not NULL AUTO_INCREMENT, University_ID int NOT NULL, Academic_Year int NOT NULL, Score int, GRE int, TOEFL int, SOP numeric(9,2), LOR numeric(9,2), CGPA numeric(9,2), Research int, FOREIGN KEY (University_ID) REFERENCES University(University_ID), PRIMARY KEY(Requirements_ID))")
mycursor.execute("CREATE TABLE Student_Profile(Student_ID int AUTO_INCREMENT, Name VARCHAR(255), Contact_Number int, Email_ID VARCHAR(255), Age int, Graduation_Year int, CGPA float, TOEFL_Score int, GRE_Score int, PRIMARY KEY (Student_ID))")
print("enddd")
print("Schema Created")