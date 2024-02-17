from flask import Flask, render_template,request
import pickle
import numpy as np#pip install numpy

app = Flask(__name__)
#load the pickle model
model = pickle.load(open("model.pkl","rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict",methods=['POST','GET'])
def predict():
    if request.method == "POST":
        '''
        method 1 for prediction in app.py
        age = request.form['age']
        weight = request.form['weight']
        # # print([age,weight])
        
        pred = model.predict([[age,weight]])
        '''
        input_float_values = [float(x) for x in request.form.values()]
        input_features =  [np.array(input_float_values)]
        pred = model.predict(input_features)
        msg = ''
        if pred[0] == 1:
            msg += "He can eat pizza"
        else:
            msg += "he can't eat pizzaa"
        
        
    return render_template("index.html",pred=msg)


if __name__=='__main__':
    app.run(debug=True)