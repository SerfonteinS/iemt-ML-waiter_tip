import pandas as pda
import numpy as npy
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
    
if __name__ == '__main__':
    tip_data = pda.read_csv("tips.csv")
    #print(tip_data.head())

    tip_data["sex"] = tip_data["sex"].map({"Female": 0, "Male": 1})
    tip_data["smoker"] = tip_data["smoker"].map({"No": 0, "Yes": 1})
    tip_data["day"] = tip_data["day"].map({"Thur": 0, "Fri": 1, "Sat": 2, "Sun": 3})
    tip_data["time"] = tip_data["time"].map({"Lunch": 0, "Dinner": 1})
    #print(tip_data.head())

    x = npy.array(tip_data[["total_bill", "sex", "smoker", "day", "time", "size"]])
    y = npy.array(tip_data["tip"])

    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(xtrain, ytrain)


    # Please enter the required values for the prediction, below on line 32 in the array:
    #  the first value is the bill total.
    #  the second value is the paying customer's gender, which is either the number 0 for female, or 1 for male.
    #  the third value is the paying customer's smoking status, which is either 0 for if they are not a smoker, or 1 for if they are.
    #  the fourth value is the day of the transaction for which the tip must be predicted, either 0 for Thursday, 1 for Friday, 2 for Saturday, or 3 for Sunday.
    #  the fifth value is the time of the transaction for which the tip must be predicted, either 0 for lunch, or 1 for dinner.
    #  the sixth value is the number of people in the group.
    
    input = npy.array([[24.50, 1, 0, 0, 1, 4]])
    print(model.predict(input))
