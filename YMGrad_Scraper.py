import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import mysql.connector


mydb = mysql.connector.connect(host="localhost", user="root", password="Sh_reyasi03")
mycursor = mydb.cursor()

mycursor.execute("Use FinalProject")

# Code for creating a soup for only a few universities

URL = "https://yocket.com/universities/masters-in-computer-science"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")


# Code wil open the browser, keep it open for 20 seconds and in that time you can keep clicking on load more button at bottom of website to load much more university data

browser = webdriver.Chrome()
browser.get(URL)
time.sleep(20)
soup = BeautifulSoup(browser.page_source, "html.parser")

# Code will extract the list of all divisions from html file where the university details are mentioned and give a count of university details loaded in html page

results = soup.find_all("div",
                        class_="relative h-full max-w-lg border bg-white border-gray-200 rounded-xl shadow-md hover:cursor-pointer transition ease-in-out md:hover:-translate-y-1 md:hover:scale-105 duration-300 hover:shadow-lg px-3 py-6")
print(len(results))

# This part of code is responsible for iterating over each div where university info is present and then extracting each information by their respective classes

for i in results:

    # Fecthes value of each attribute to be extracted by the class of the tag they are present in

    uni_name = i.find("p",
                      class_="cursor-pointer hover:text-yocketPrimary hover:underline text-base font-semibold text-yocket-neutral-900")
    location = i.find("p", class_="text-sm text-yocket-neutral-500")
    course = i.find("p",
                    class_="text-yocket-neutral-900 hover:text-yocketPrimary text-sm font-bold hover:underline cursor-pointer")
    scholarships = i.find_all("span", class_="text-sm text-yocket-neutral-900 font-semibold")
    avg_tution_fees = i.find("span", class_="text-yocket-neutral-900 text-sm font-bold")

    # Populates the attributes as "Info not available" if the value is not found from the html page

    if (uni_name == None):
        uni_name = "Info Not Available"
    else:
        uni_name = uni_name.get_text().strip()
    if (avg_tution_fees == None):
        avg_tution_fees = "Info Not Available"
        x1[0] = 0;
    else:
        avg_tution_fees = avg_tution_fees.get_text().strip()
        print(avg_tution_fees)
        # x= re.split("\$ | £", avg_tution_fees)

        x = avg_tution_fees.split("£")
        print(len(x))
        if len(x) == 1:
            x = avg_tution_fees.split("€")
            print("-----------------------", x)
        if len(x) == 1:
            x = avg_tution_fees.split("$")
        if len(x) == 1:
            x = ['0', '0/0']
        x1 = x[1].split("/")
        print(x1[0])

    if (location == None):
        location = "Info Not Available"
    else:
        location = location.get_text().strip()
    if (course == None):
        course = "Info Not Available"
    else:
        course = course.get_text().strip()
    if (scholarships == None or scholarships == [] or scholarships == " "):
        scholarships = "Info Not Available"
    else:
        scholarships = scholarships[-1].get_text().strip()

# Prints all the values extracted from the html page

    print("University Name : ", uni_name)
    print("University Location : ", location)
    print("Course Offered : ", course)
    print("Scholarship Status : ", scholarships)
    print("Average Tuition Fee : ", avg_tution_fees)
    print("\n")
    val = str(x1[0])
    print(type(uni_name))
    update_sql = "Update University set tuition_fees = %s where University_name = %s;"
    update_val = (int(val.replace(',', '')), uni_name)
    mycursor.execute(update_sql,update_val)

mydb.commit()

# Creating view of university requirements
mycursor = mydb.cursor(buffered=True)

sql1 = "create view University_Requirement as Select university.University_ID, University_name, GRE, TOEFL, SOP, LOR, CGPA, Research from University inner join Requirements on University.University_Id = Requirements.University_ID"
mycursor.execute(sql1)

sql2= "Select * from University_Requirement"
mycursor.execute(sql2)

# Acceptance rate of university based on GRE score
sql3 = "Create view acceptance_GRE as Select University.University_ID, University_name, GRE, Chance_of_Admit from University inner join Requirements on University.University_ID = Requirements.University_ID"
mycursor.execute(sql3)
sql4= "Select * from acceptance_GRE"
mycursor.execute(sql4)
record = mycursor.fetchone()
print(record)

sql5 = "Create View employment_rate AS Select University.university_ID, University_name, Alumni_Employement from University inner join Standards on University.University_ID = Standards.University_ID"
mycursor.execute(sql5)
sql6= "Select * from employment_rate"
mycursor.execute(sql6)
record = mycursor.fetchone()
print(record)