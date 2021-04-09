import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot

header = ["Year", "Quarter", "Primary and below", "Lower secondary", "Upper secondary",
          "Post-secondary", "Post-secondary : Diploma / Certificate", "Post-secondary : Sub-degree",
          "Post-secondary : Degree", "overall"]

df = pd.read_excel("income.xlsx", sheet_name=0, skiprows=6, header=None)
df = df.dropna(axis=1, how='all')
df.columns = header
databyyear = df[np.isnan(df['Quarter'])]  # Quarter is empty
databyyear = databyyear.set_index('Year')
databyyear.drop(['Quarter'], axis=1, inplace=True)


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

