from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Sh_reyasi03")
mycursor = mydb.cursor()

mycursor.execute("Use finalproject")
data=pd.read_csv(r"D:\DMDD\Assignment 3\University_Name_and_Details.csv")

x=data[['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR ', 'CGPA','Research', 'Score', 'National_Rank' ]]
y=data[['Chance of Admit ']]

model=LinearRegression()
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=11)
model.fit(x_train,y_train)
Ypredic=model.predict(x_test)
df=y_test.copy()
df['Predicted Values']=Ypredic
df.columns=['Actual Values','Predicted Values']
print(df)

print("Accuracy of this model is : ", r2_score(y_test,Ypredic))
#test_case=model.predict([[320,100,5, 1, 3, 3.6, 1, 44.51,2 ]])
#print("Chance of admit of a student with GRE score - 320, TOEFL Score - 100 in a university having 5 rating is : ", test_case)

#Visualization for prediction
sns.distplot(y_test,hist=False,label='y_test')
sns.distplot(Ypredic,hist=False,label='Ypredic')
plt.legend()
plt.show()


print("UNIVERSITY SHORTLISTING AND PREDICTION")
name = input('\nEnter name: \n')
age = input('\nEnter age: \n')
contact_no = input('\nEnter contact no: \n')
emailid = input('\nEnter email id: \n')
grad_year = input('\nEnter graduation year: \n')
gpa = input('\nEnter CGPA: \n')
toefl = input('\nEnter toefl: \n')
gre = input('\nEnter GRE: \n')

type_of_uni = input("\nWhich type of university are you looking for ?\n1. Ambitious\n2. Moderate \n3. Safe \n")

if type_of_uni == "1":
    sql = """Select University.university_ID, University_name, GRE from university right join requirements on University.university_Id = Requirements.University_ID where GRE > %s"""
    val = (gre,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
elif type_of_uni == "2":
    sql = """Select University.university_ID, University_name, GRE from university right join requirements on University.university_Id = Requirements.University_ID where GRE = %s"""
    val = (gre,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

else :
    sql = """Select University.university_ID, University_name, GRE from university right join requirements on University.university_Id = Requirements.University_ID where GRE < %s"""
    val = (gre,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

print(name, ", your chance of admit for intake 2023 is: ")
test_case1=model.predict([[int(gre),int(toefl),5, 1, 3, float(gpa), 1, 44.51,2 ]])
print(test_case1)

insert =  ("insert into student_profile( Name , Contact_Number , Email_ID , Age , Graduation_Year, CGPA , TOEFL_Score , GRE_Score) values(%s,%s,%s,%s,%s,%s,%s,%s)")
values = (name, contact_no,emailid,age,grad_year,gpa,toefl,gre)
mycursor.execute(insert, values)
mydb.commit()