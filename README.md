# iemt-ML-waiter_tip

# Code explanation:

I used the pandas library for its IO tools, which in my case includes the loading of my CSV file (tips.csv) containing my dataset.

I used the numpy library to create array objects to store and manipulate my dataset (tips.csv)

I mapped some of my dataset values (the values that were not numeric), for example my "day" and "sex" (gender) values, to numeric values starting from 0, and incrementing by 1. By mapping these values, it made it possible for me to request input values from the user in numeric form. This minimizes the possibility for spelling mistakes and incorrect data types, as words will not be required (which usually needs to be spelled correctly for code to work). 

I created 2 arrays using the numpy library named "x" and "y". "x" contained the variables that the user must input values to in order to predict a tip. "y" contained the 'tip' variable, which is the ultimate result/tip received. 

I used the "train_test_split" function to create 4 random arrays, 2 for training, and 2 for testing. Both the training and the testing sets each have an "x" and "y" set, which means 1 "x" training, 1 "y" training, 1 "x" testing, and 1 "y" testing set. As described by their names, these 4 sets are used to train, and to test the machine learning system, so that users can use it to predit waiter tips.

I used the sklearn library (now called scikit-learn), more specifically the LinearRegression vie of the linear_model part of the library, to train the machine learning system to predict waiter tips. 


# System usage instructions:

I included the necessary requirements for this machine learning system to work in the "requirements.txt" file. These libraries need to be installed for the system to work.

In line 32, the user must enter the values in the array for which a prediction must be made:
- The first value must be a numeric value (int or float) which indicates the total for the bill that the customer must pay BEFORE adding the tip.
- The second value represents the paying customer's gender, which is either the numeric value of 0 for a female, or the numeric value for a male.
- The third value represents the paying customer's smoking habits, which is either the numeric value of 0 if the customer does NOT smoke, or the numeric value of 1 if the customer does indeed smoke.
- The fourth value represents the day of the week for which the tip prediction must be made. The options are either the numeric value of 0 for Thursday, thh numeric value of 1 for Friday, the numeric value of 2 for Saturday, or the numeric value of 3 for Sunday. This system only does tip predictions for days Thursday to Sunday. 
- The fifth value represents the time of day for which the tip must be predicted. The options are either the numeric value of 0 for lunch, or the numeric value of 1 for dinner.
- The sixth and final value represents the 'size' of the group of customers.

When the user enters their values into the array and run the system, the system will output the predicted tip for the waiter/waitress in the float format.

If the user would like to make a new prediction, then he/she must just enter the new values for the prediction, and then run the system again to receive a new prediction value.
