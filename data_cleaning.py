

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("messy_data_cleaning_20_rows.csv")


print(df.info())
print(df.isna().sum())
print(df.duplicated().sum())


df= df.drop_duplicates()

print(df.duplicated().sum())


df["Name"] = df["Name"].str.strip()
df["City"] = df["City"].str.strip()
df["Email"] = df["Email"].str.strip()


df["City"] = df["City"].str.title()


df["Gender"] = df["Gender"].replace({

    "M": "Male",
    "F": "Female",
    "male": "Male",
    "female": "Female"
})


df["Age"] = df["Age"].replace({

     "twenty-one": "21",
     "twenty-three": "23"
})


df["Age"] = pd.to_numeric(df["Age"],errors="coerce")


df["Age"] = df["Age"].fillna(df["Age"].median())

df["Salary"] = pd.to_numeric(df["Salary"],errors="coerce")

df["Salary"] = df["Salary"].fillna(df["Salary"].median())


df["Join_Date"] = pd.to_datetime(df["Join_Date"],errors="coerce")


print(df.isnull().sum())


print(df)

df.plot(x="Age",y="Salary",kind="bar")
plt.show()


sns.barplot(data=df,x="Age",y="Salary",hue="City")
plt.show()
