import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

ds=pd.read_csv(r"D:\DMDD\Assignment 3\University_Name_and_Details.csv")
# print(ds.columns)
# pd.set_option('display.max_columns', None)
col = ds[["Serial No", "Institution", "National_Rank"]]
print(ds.info())
# print(col.head())
# print("-----------------------------------------------------------------------------")

#sorting the dataset based on national ranking
sorted_ds = ds.sort_values('National_Rank', ascending=True, kind='heapsort', na_position='last')
sorted_ds.head()
colout = sorted_ds[["Serial No", "Institution", "National_Rank"]]
# print(colout.head())

#ascending= True means asc oredr
#kind ---- kind of sorting method used
#na_position ----null values of not a number values will be placed in last

#data reduction
ds.drop(["publications", "influence", "citations", "broad_impact"], axis=1, inplace = True )
# pd.set_option('display.max_columns', None)
print(ds.drop)

#Audit Completeness
for col in ds.columns:
    miss = ds[col].isnull().sum()
    if miss>0:
        print("{} has {} missing value(s)".format(col,miss))
    else:
        print("{} has NO missing value!".format(col))



# data completeness
output_ds = pd.DataFrame(columns=['Count', 'Missing', 'Unique', 'Dtype', 'Mean', 'Mode', 'Min', '25%', 'Median', '75%', 'Max', 'Std', 'Skew'])
for col in ds:
    if pd.api.types.is_numeric_dtype(ds[col]):
        output_ds.loc[col] = [ds[col].count(), ds[col].isnull().sum(), ds[col].nunique(), ds[col].dtype, ds[col].mean(), ds[col].mode(), ds[col].min(), ds[col].quantile(0.25), ds[col].median(), ds[col].quantile(0.75), ds[col].max(), ds[col].std(), ds[col].skew()]
    else:
        output_ds.loc[col] = [ds[col].count(), ds[col].isnull().sum(), ds[col].nunique(), ds[col].dtype, '-', '-', '-', '-', '-', '-', '-', '-', '-']
#pd.set_option('display.max_columns',100)
#pd.set_option('display.max_rows',100)
print(output_ds)

#validity and accuracy
#GRE score validation
total_rows = 400
print("\n\nValidating GRE Score")
sum = ds['GRE Score'].between(260, 340).sum()
print("Count of accurate rows for GRE Score : ",sum)
print("Percentage of GRE Score accuracy : ",(sum/total_rows)*100,"%")

#TOEFL Score Validation
print("\n\nValidating IELTS Score")
sum = ds['TOEFL Score'].between(80, 120).sum()
print("Count of accurate rows for TOEFL Score : ",sum)
print("Percentage of TOEFL Score accuracy : ",(sum/total_rows)*100,"%")

#CGPA Validation:
print("\n\nValidating CGPA")
sum = (ds['CGPA'].between(5, 10).sum())
print("Count of accurate rows for CGPA : ",sum)
print("Percentage of CGPA Score accuracy : ",(sum/total_rows)*100,"%")

#Chances of Admit:
print("\n\nValidating Chance of Admit")
sum = (ds['Chance of Admit '].between(0, 1).sum())
print("Count of accurate rows for CGPA : ",sum)
print("Percentage of Chance of Admit accuracy : ",(sum/total_rows)*100,"%")


#Uniqueness in University Name:
print("\n\nChecking uniqueness in Dataset")
sum = output_ds['Unique'][1]
if(sum==400):
    print("Institute name Field is unique by : ", (sum/total_rows)*100,"%")

#Uniqueness in University ID:
sum = output_ds['Unique'][0]
if(sum==400):
    print("University ID Field is unique by : ", (sum/total_rows)*100,"%")


#Inserting data in the tables.
#pd.set_option('display.max_columns', None)
print(ds)
university = ds[["Serial No", "Institution", "Country", "National_Rank", "University Rating","Chance of Admit "]]
standards = ds[["Serial No","Quality_of_Education", "Alumni_Employment", "Quality_of_Faculty", "Patents"]]
requirements = ds[["Serial No","Academic_Year", "Score", "GRE Score", "TOEFL Score", "SOP", "LOR ","CGPA", "Research"]]

mydb = mysql.connector.connect(host="localhost", user="root", password="Sh_reyasi03")
mycursor = mydb.cursor()
mycursor.execute("Use finalproject")


# Trigger to count total number of universities
#mycursor.execute("SET @count = 0");
#mycursor.execute("create trigger count_uni BEFORE INSERT ON University FOR EACH ROW SET @count = @count +1")

#user_val = ("2", "abc", "USA", "1", "1")
university_sql = "INSERT INTO University(University_ID, University_Name, Country, National_Rank, University_Rating, Chance_of_Admit)VALUES (%s, %s, %s, %s, %s, %s)"
#mycursor.execute(user_sql, user_val)

mycursor.execute("SET GLOBAL event_scheduler = ON;")
mycursor.execute("CREATE EVENT test ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 1 Minute  COMMENT 'Clears out sessions table each hour.' DO  begin INSERT INTO Data VALUES('asd', 25); update data set age = 10  where (name = 'asd'); End")

for i in range(len(university)):
    university_val = (university.iloc[i, 0].astype(str), university.iloc[i, 1], university.iloc[i, 2] ,university.iloc[i, 3].astype(str),university.iloc[i, 4].astype(str),university.iloc[i, 5 ].astype(str))
    mycursor.execute(university_sql, university_val)


print(requirements)
requirements_sql = "INSERT INTO Requirements(University_ID, Academic_Year, Score, GRE, TOEFL, SOP, LOR, CGPA, Research)VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s)"
for i in range(len(requirements)):
    requirements_val = (requirements.iloc[i,0].astype(str), requirements.iloc[i,1].astype(str), requirements.iloc[i,2].astype(str), requirements.iloc[i,3].astype(str), requirements.iloc[i,4].astype(str), requirements.iloc[i,5].astype(str), requirements.iloc[i,6].astype(str), requirements.iloc[i,7].astype(str), requirements.iloc[i,8].astype(str))
    mycursor.execute(requirements_sql, requirements_val)

print(standards)
Standards_sql = "INSERT INTO Standards(University_ID, Quality_of_Education, Alumni_Employement, Quality_of_Faculty, Patent)VALUES (%s, %s,%s,%s,%s)"
for i in range(len(standards)):
    Standards_val = (standards.iloc[i,0].astype(str), standards.iloc[i,1].astype(str), standards.iloc[i,2].astype(str), standards.iloc[i,3].astype(str), standards.iloc[i,4].astype(str))
    mycursor.execute(Standards_sql, Standards_val)

mydb.commit()
print("Trigger : to calculate count of university.")
mycursor.execute("SELECT @count AS count_university")
print(mycursor.fetchall())

