import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot

header = ["Year", "Quarter", "Primary and below", "Lower secondary", "Upper secondary",
          "Post-secondary", "Post-secondary : Diploma / Certificate", "Post-secondary : Sub-degree",
          "Post-secondary : Degree", "overall"]
year = [2014,2015,2016,2017,2018,2019]

df = pd.read_excel("income.xlsx", sheet_name=0, skiprows=6, header=None)
df = df.dropna(axis=1, how='all')
df.columns = header
databyyear = df[np.isnan(df['Quarter'])]  # Quarter is empty
databyyear = databyyear.set_index('Year')
databyyear.drop(['Quarter'], axis=1, inplace=True)

degree_population = pd.DataFrame({'Degree course': [22.0,23.3,24.0,24.8,25.4,25.3]},index=year)
subdegree_population = pd.DataFrame({'Sub-Degree course': [4.7,4.8,5.0,5.0,5.2,5.4]},index=year)
diploma_population = pd.DataFrame({'Diploma course': [3.2,2.7,2.6,2.4,2.5,3.2]},index=year)
secondary_population = pd.DataFrame({'Secondary': [50.5,50.2,49.7,49.7,49.0,48.1]},index=year)
primary_population = pd.DataFrame({'Primary and below': [19.7,18.9,18.7,18.2,17.9,18.0]},index=year)

degree_salary = databyyear.loc[year,["Post-secondary : Degree"]]
subdegree_salary = databyyear.loc[year,["Post-secondary : Sub-degree"]]
diploma_salary = databyyear.loc[year,["Post-secondary : Diploma / Certificate"]]
secondary_salary = pd.DataFrame(databyyear.loc[year,["Upper secondary", "Lower secondary"]].mean(axis=1))
secondary_salary.columns=["aaaa"]
primary_salary = databyyear.loc[year,["Primary and below"]]

databyyear.plot()
plt.title(" Median monthly employment earnings of employed persons by educational attainment") # title
plt.ylabel("Median monthly employment earnings") # y label
plt.xlabel("Year") # x label

plt.rcParams['figure.figsize'] = (16.0, 12.0)
plt.savefig('line.png')
plt.show()
plt.clf()

lag_plot(databyyear)
plt.rcParams['figure.figsize'] = (16.0, 12.0)
plt.savefig('dot.png')
plt.show()

