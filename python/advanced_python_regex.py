import numpy as np
import pandas as pd
import csv
f = open('faculty.csv')
csv_f = csv.reader(f)
faculty_pd = pd.read_csv('faculty.csv')

#print faculty_pd.index
#print faculty_pd.columns

names = []
degrees = []
titles = []
emails = []
domains = []

#Q1
degree_table = pd.crosstab(index=faculty_pd[" degree"], columns="count")
print degree_table

#Q2
title_table = pd.crosstab(index=faculty_pd[" title"], columns="count")
print title_table

#Q3
for i in csv_f: 
    names.append(i[0])
    degrees.append(i[1])
    titles.append(i[2])
    emails.append(i[3])
emails_no_header = emails[1:]
print emails_no_header

#Q4
emails_split = map(lambda x: x.split('@'), emails_no_header)
for x in emails_split:
    domains.append(x[1])

domains_pd = pd.Series(domains)

domains_table = pd.crosstab(domains_pd, columns="count")

print domains_table
