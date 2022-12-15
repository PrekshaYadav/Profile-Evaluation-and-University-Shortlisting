import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ds=pd.read_csv(r"D:\DMDD\Assignment 3\University_Name_and_Details.csv")
# print(ds.columns)
# pd.set_option('display.max_columns', None)
col = ds[["Serial No", "Institution", "National_Rank"]]
print(ds.info())
# print(col.head())
# print("-----------------------------------------------------------------------------")

#Visualization
#Grouping country
Country = ds.groupby('Country')['Serial No'].nunique()
countryName = []
countryCount = []
for i,v in Country.items():
    countryName.append(i)
    countryCount.append(v)
colors = sns.color_palette('pastel')[0:5]
plt.pie(countryCount, labels = countryName, colors = colors, autopct='%.2f')
plt.show()

#Checking the chance of admit and university ranking
sns.boxplot(x=ds['University Rating'],y=ds['Chance of Admit '])
plt.show()

#Checking the chance of admit on the basis of GRE score
plt.figure(figsize=(20,7))
sns.lineplot(x=ds['GRE Score'],y=ds['Chance of Admit '])
plt.show()

#Checking the chance of admit on the basis of TOEFL score
plt.figure(figsize=(20,7))
sns.boxplot(x=ds['TOEFL Score'], y=ds['Chance of Admit '])
plt.show()