import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 =pd.read_csv("C:/Users/Admin/.spyder-py3/Assessment/college_1.csv")

df2 = pd.read_csv("C:/Users/Admin/.spyder-py3/Assessment/college_2.csv")

df = df1.merge(df2,how="outer")

# df.to_csv("C:/Users/Admin/.spyder-py3/Assessment/combine.csv")

#consider if the codekata score exceeds 15000 points(present week) then make a csv on those observations as Exceeded expectations.csv


df3 = df[df['CodeKata Score'] > 15000].set_index('Name')

df3.to_csv("Exceeded expectations.csv")


#if  10000<codekata score<15000   (Reached_expectations.csv)


df4 = df[(df['CodeKata Score'] > 10000) & (df['CodeKata Score'] < 15000)].set_index('Name')


df4.to_csv("Reached_expectations.csv")


# if  7000<codekata score<10000   (Needs_Improvement.csv)

df5 = df[(df['CodeKata Score'] > 7000) & (df['CodeKata Score'] < 10000)].set_index('Name')

df5.to_csv("Needs_Improvement.csv")

#if codekate score < 7000 (Unsatisfactory.csv)

df6 = df[df['CodeKata Score'] < 7000].set_index('Name')

df6.to_csv("Unsatisfactory.csv")

#Average of previous week geekions vs this week geekions (i.e Previous Geekions vs CodeKata Score)

print("Average of previous week geekions:",df['Previous Geekions'].mean())
print("Average of This week geekions:",df['CodeKata Score'].mean())

#No of students participated

print("No of students participated:",df['Name'].count())

#Average completion of python course or my_sql or python english or computational thinking

print("Average completion of python course :",df['python'].mean())

#rising star of the week (top 3 candidate who performed well in that particular week)

print(df.sort_values(by=['Rising'],ascending=False).head(3).set_index('Name'))

#Shining stars of the week (top 3 candidates who has highest geekions)

print(df.sort_values(by=['Previous Geekions'],ascending=False).head(3).set_index('Name'))

###### Department wise codekata performence (pie chart)

df7 = df.groupby(['Department'])

df8 = df7.sum()

x=df.Department.unique()
y=df8['CodeKata Score']

plt.pie(y,labels=x,autopct='%1.2f%%')

plt.show()



#Department wise toppers (horizantal bar graph or any visual representations of your choice)

df12 = df.loc[df.Department=='Computer Science and Engineering',['Name','CodeKata Score','Department']]
csc_top = df12.sort_values(by='CodeKata Score',ascending=False)
csc_top = csc_top.head(3)

print(csc_top)

df13 = df.loc[df.Department=='Electronics and Communication Engineering',['Name','CodeKata Score','Department']]
ece_top = df13.sort_values(by='CodeKata Score',ascending=False)
ece_top = ece_top.head(3)

print(ece_top)

df14 = df.loc[df.Department=='Electronics and Electrical Engineering',['Name','CodeKata Score','Department']]
eee_top = df14.sort_values(by='CodeKata Score',ascending=False)
eee_top = eee_top.head(3)

print(eee_top)

topp_df = csc_top.merge(ece_top,how="outer")
topp_df = topp_df.merge(eee_top,how="outer")

print(topp_df)




w=0.2

x = topp_df['Department'].unique()



CSE =[24500,21740,19680]
ECE=[10040,8650,7880]
EEE=[19400,9150,8320]


CSE_bar=ece_top['Name']
ECE_bar=eee_top['Name']
EEE_bar=eee_top['Name']

CSE_bar=np.arange(len(x))
ECE_bar=[i+w for i in CSE_bar]
EEE_bar=[i+w for i in ECE_bar]



plt.bar(CSE_bar,CSE,w,label="CSE")
plt.bar(ECE_bar,ECE,w,label="ECE")
plt.bar(EEE_bar,EEE,w,label="EEE")

plt.xlabel("Student's Name")
plt.ylabel("CodeKata Score")

plt.title("Department's wise topper's")
plt.legend()
plt.show()

print("\n")
