#1.import Packages
import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


#reading the csv(dataset)
df = pd.read_csv('exam.csv')
print(df)

#seperate input and output
X = df[["Hours"]]#input # df.iloc[:-1]
# X= df.iloc[:-1]
# print(X)
y = df["CGPA"]
# y = df.iloc[-1]
# print(y)


#splitting the dataset into traing and testing
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=5)


#calling algirithm
model = LinearRegression()
#traing the model
model.fit(X_train,y_train)


#predict the outp
pred = model.predict([[14]])#2d array as input while predicting
print("model predicted as: ",pred[0])


