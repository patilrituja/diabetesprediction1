from flask import Flask, render_template,jsonify,request
from utils import Diabetese_Prediction
import pickle
import traceback
import config1
import utils


app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST',"GET"])
def predict():
    try :
        if request.method == "POST":
            data = request.form.get
            Glucose= eval(data('Glucose'))
            BloodPressure = eval(data('BloodPressure'))
            SkinThickness= eval(data('SkinThickness'))
            Insulin= eval(data('Insulin'))
            BMI = eval(data('BMI'))
            DiabetesPedigreeFunction= eval(data('DiabetesPedigreeFunction'))
            Age= int(data('Age'))

            dia_predict = Diabetese_Prediction(Glucose, BloodPressure, SkinThickness, Insulin, BMI,
                                    DiabetesPedigreeFunction, Age)
            
            predict_class = dia_predict.prediction()
            
            if predict_class == [1]:
                    predict_class = "diabetes"

            else:
                    predict_class = "Normal"
            if predict_class == "diabetes":
                return render_template('index.html',prediction = predict_class)
            else:
                return render_template('result.html',prediction = predict_class)
        else :
            data = request.args.get
            Glucose= eval(data('Glucose'))
            BloodPressure = eval(data('BloodPressure'))
            SkinThickness= eval(data('SkinThickness'))
            Insulin= eval(data('Insulin'))
            BMI = eval(data('BMI'))
            DiabetesPedigreeFunction= eval(data('DiabetesPedigreeFunction'))
            Age= int(data('Age'))

            dia_predict = Diabetese_Prediction(Glucose, BloodPressure, SkinThickness, Insulin, BMI,
                                    DiabetesPedigreeFunction, Age)
            
            predict_class = dia_predict.prediction()
            
            if predict_class == [1]:
                    predict_class ="diabetes"

            else:
                    predict_class ="Normal"
            if predict_class == "diabetes":
                return render_template('result.html',prediction = predict_class)
            else:
                return render_template('result.html',prediction = predict_class)
    except :
        print(traceback.print_exc())
        return jsonify({"message" : "unsuccessful"})

if __name__== "__main__":
    app.run(host='0.0.0.0',port = config1.PORT_NUMBER, debug=False)