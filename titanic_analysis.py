import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")
print(df.head())
print(df.shape)
print(df["Sex"].value_counts())
print(df["Age"].mean())
print(df["Survived"].value_counts())
survived = df["Survived"].mean() * 100
print(survived)
print(df.groupby("Sex")["Survived"].mean() * 100)
print(df.groupby("Pclass")["Survived"].mean() * 100)
df["Sex"].value_counts().plot(kind="bar")
plt.title("Male vs Female")
plt.show()
print("=== PROJECT SUMMARY ===")

print("=== PROJECT SUMMARY ===")

print("Total Passengers:", df.shape[0])
print("Average Age:", df["Age"].mean())
print("Survival Rate:", df["Survived"].mean() * 100, "%")

git commit -m