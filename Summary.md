# Project Report for Info 16149 - Data Management and Data Design


## Topic Name:  
Profile Evaluation and University Shortlisting
<br />

1) Data collection :
Dataset which was required for this project is gathered in a form of CSV file from Kaggle and by web scrapping ("YMGrad" website). The scraped data was then merged in the CSV file based on the university name in the file.


CSV file reference : Kaggle.com

Web scrapping : YMGrad.com



2) Data cleaning :
The dataset which was gathered was cleaned. All the unnecessary columns were removed from the dataset. Handled all the null values.

![Class Diagram](images/Data_Reduction-1.png)
![Class Diagram](images/Data_Reduction-2.png)


3) Audit :
Performed audit check on the dataset collected.
    - Checked correctness of the data.
    - Checked validation of the data
    - Verified uniqueness of the dataset
    - Validated accuracy of the data collected
    - Determined completness of the dataset

Null value check:

![Class Diagram](images/Audit_completeness-2.png)


Data completness output:

![Class Diagram](images/data_completness.png)

Data validity :

![Class Diagram](images/validity.png)

Data Uniqueness:

![Class Diagram](images/uniqueness.png.jpg)


4) Data insertion :
After cleaning and audting, the data is inserted into the respective tables using mysql connector through python. The schema that was created is :
![Class Diagram](images/University.png)
![Class Diagram](images/Standards.png)
![Class Diagram](images/requirements.png)
![Class Diagram](images/student_profile_table.png)



5) SQL Queries :
    - Views
        1. View for university requirements. (Joining University and REquirements table)
            ![Class Diagram](images/view1.png)
        2. View for University name, GRE score and acceptance rate.
            ![Class Diagram](images/view3.png)
        3. View for the university and employment rate. (Joining University and Standards table)
            ![Class Diagram](images/view2.png)


    - Triggers
        1. Created trigger to enter 0 in Requirements table after each entry in University table.

                Output : 

                INSERT INTO University(University_ID, University_Name, Country, Chance_of_Admit, University_Rating, National_Rank)VALUES ('402', 'test', 'test', '1000', '1000', '1000');

            ![Class Diagram](images/trigger1.png)
            ![Class Diagram](images/trigger2.png)
        
        2. Trigger to calculate count of university inserted.That count can be used for evaluation.

                Output : 
                After inserting the records in the table,
            ![Class Diagram](images/trigger3.png)





    - Procedures
        1. Procedure to fetrch the university requirements of a specific university.
            
            Output :
            ![Class Diagram](images/procedure1.png)

    - Indexes

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

        ![Class Diagram](images/index1.png)
        ![Class Diagram](images/index2.png)
        ![Class Diagram](images/index3.png)


6) Visualization:
Performed visualization for the collected data. For visualization we have used Seaborn and matplotlib.

    - Boxplot :
    Implemented boxplot graph for University rating and Chance of Admit. Representing chance of rating depending upon chance of admit.
    ![Class Diagram](images/Visualization/Chance_of_Admit_on_the_basis_of_University_Rating.png)


    - Lineplot : 
    Represented chance of admit based on GRE score using Lineplot graph.
    ![Class Diagram](images/Visualization/diag1.png)


    - Figure : 
    Analysed chance of admit based in the Figure graph.
    ![Class Diagram](images/Visualization/diag2.png)

    - Pie Chart
    Represented number of university in various Countries.
    ![Class Diagram](images/Visualization/diag3.png)

6) Prediction : Linear Regression
Performed linear regression to predict the chance of admit based on the given profile. Trained a model using 70% of the dataset available and then performed testing using the remaining dataset i.e 30%.
![Class Diagram](images/Visualization/YPredict.png)

Accuracy of the developed model is : 0.728

Given a User profile the chance of admit predicted is :
![Class Diagram](images/Visualization/Prediction.png)


7) Backup and Restore
We have also taken a backup of our database. So that in case of any causality we can restore it.
![Class Diagram](images/Backup-1.png)
![Class Diagram](images/Backup-2.png)
![Class Diagram](images/Database_deleted.png)
![Class Diagram](images/restore-1.png)
![Class Diagram](images/restore-2.png)
![Class Diagram](images/db_restored.png)

8) User Interface:
User will first register in the website.
![Class Diagram](images/register.jpg)

User will then login into the website using his credentials.
![Class Diagram](images/login_page.jpg)

Once the user logs in, he can seach for the universities based on his profile by entering his GRE score, TOEFL score and CGPA 

![Class Diagram](images/search1.jpg)
![Class Diagram](images/search2.jpg)

User can also search the university by giving university name which will give all the details of the searched university.

![Class Diagram](images/serach3.jpg)













