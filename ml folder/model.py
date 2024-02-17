#1.import Packages
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


#reading the csv(dataset)
df = pd.read_csv('pizza.csv')
print(df)

#seperate input and output
X = df[["age","weight"]]#input # df.iloc[:-1]
# X= df.iloc[:-1]
# print(X)
y = df["buy_pizza"]
# y = df.iloc[-1]
# print(y)


#splitting the dataset into traing and testing
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=5)


#calling algirithm
model = RandomForestClassifier()
#traing the model
model.fit(X_train,y_train)


#predict the outp
pred = model.predict([[26,97]])#2d array as input while predicting
print("model predicted as: ",pred[0])

if pred[0] == 1:
    print("Enjoy pizza")
    
else:
    print("Go gym")

