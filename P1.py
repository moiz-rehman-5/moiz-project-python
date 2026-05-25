# P-1  sunday May 4 2026  5:44 AM
"""
Student Performance Analyzer (Excel-style real work)

Scenario: You are a data intern in a training company.

What you do:
Load CSV of students marks
Clean missing values
Calculate:
average marks
top students
pass/fail ratio
"""

import pandas as pd 

data = pd.read_csv(r"C:\Users\MOIZ\Desktop\CsV files\student_performance_raw.csv")
df = pd.DataFrame(data)

df = df.drop_duplicates()
df = df.dropna()
df.columns = df.columns.str.strip()
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" " , "_")
avrage_marks = df.groupby("student_name")["obtained_marks"].mean()
top_student = avrage_marks.idxmax()
print(df.columns)
print(df.isnull().sum())
print(df)
print(df.head())
print(df.info())
print(df.describe())
print(avrage_marks)
print(top_student)

result = avrage_marks.apply(lambda x: "PASS" if x >= 60 else "FAIL")
print(result)
df.to_csv("student performance cleaned.csv",index=False)
#--------ended-----------