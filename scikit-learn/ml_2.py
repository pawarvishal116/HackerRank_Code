import pandas as pd
from sklearn.ensemble import RandomForestClassifier

data = pd.read_excel("iris-train.xlsx")

# separate features and labels
#X = Questions / Inputs
#Y = Answers

x = data.iloc[:, :-1]  # All rows and columns except the last column as features
y = data.iloc[:, -1]   # All rows and last column as labels/target

model = RandomForestClassifier()  # empty model
model.fit(x.values,y.values)     # model learn the relationship between X and Y.

#predictions = model.predict(x) 
#print(predictions)

#### So, we have train our model on iris-train.xlsx data .
# Now we are not mentioning about y in below code . 
# Above train data will now predict our iris-test.xlsx data output.

data_test = pd.read_excel("iris-test.xlsx")
x_test = data_test.iloc[:, :-1]
predictions = model.predict(x_test.values)
print(predictions)


### Calculating accuracy now by comparing last column with predicted data

y_test = data_test.iloc[:, -1]
actual = y_test.values

count = 0
for i in range(0, len(actual)):
    if actual[i] == predictions[i]:
        count = count + 1
accuracy = (count *100)/len(actual)
print(f"accuracy is {accuracy}")

'''

                TRAINING

        X                       Y
        ↓                       ↓
  measurements             known answer
        ↓                       ↓
        └─────── MODEL ─────────┘
                    ↓
              learns patterns


                PREDICTION

        NEW X
          ↓
       MODEL
          ↓
     predicted Y

'''
