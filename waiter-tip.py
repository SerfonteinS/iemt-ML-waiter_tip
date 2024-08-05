import pandas as pda
import numpy as npy
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

tip_data = pda.read_csv("tips.csv")
#print(tip_data.head())

tip_data["sex"] = tip_data["sex"].map({"Female": 0, "Male": 1})
tip_data["smoker"] = tip_data["smoker"].map({"No": 0, "Yes": 1})
tip_data["day"] = tip_data["day"].map({"Thur": 0, "Fri": 1, "Sat": 2, "Sun": 3})
tip_data["time"] = tip_data["time"].map({"Lunch": 0, "Dinner": 1})
print(tip_data.head())

x = npy.array(tip_data[["total_bill", "sex", "smoker", "day", "time", "size"]])
y = npy.array(tip_data["tip"])

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(xtrain, ytrain)

input = npy.array([[24.50, 1, 0, 0, 1, 4]])
print(model.predict(input))
