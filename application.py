from flask import Flask,request,render_template
from flask import Response
import pickle
import numpy
import pandas 

application = Flask(__name__)

app=application

scaler= pickle.load(open('models/scaler-1.pkl','rb'))
model= pickle.load(open('models/diamodel.pkl','rb'))




@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/predict",methods=['GET','POST'])
def predict():

    if request.method=='POST':
        Pregnancies=int(request.form.get("Pregnancies"))
        Glucose = float(request.form.get('Glucose'))
        BloodPressure = float(request.form.get('BloodPressure'))
        SkinThickness = float(request.form.get('SkinThickness'))
        Insulin = float(request.form.get('Insulin'))
        BMI = float(request.form.get('BMI'))
        DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction'))
        Age = float(request.form.get('Age'))

        new_data= sacler.transform([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        predict=model.predict(new_data)

        if predict[0]==1:
            result='Diabetic'
        else:
            result='Non-Diabetic'

        return render_template('singlepredict.html')



    else:
        return render_template('home.html')


if __name__=="__main__":
    app.run(host="0.0.0.0")
