import pickle
import json
import config1
import numpy as np
import pandas as pd

class Diabetese_Prediction():
    
    def  __init__ (self,Glucose, BloodPressure, SkinThickness, Insulin, BMI,
                             DiabetesPedigreeFunction, Age):
        self.Glucose = Glucose
        self.BloodPressure = BloodPressure
        self.SkinThickness = SkinThickness
        self.Insulin = Insulin
        self.BMI = BMI
        self.DiabetesPedigreeFunction = DiabetesPedigreeFunction
        self.Age = Age
    
    
    # loading model
    def __load_model(self):
        # load model file
        with open(config1.MODEL_FILE_PATH,"rb") as f:
            self.model = pickle.load(f)
        
        with open(config1.SCALER_PATH,"rb") as f:
            self.scaler = pickle.load(f)
            
            
    def prediction(self):
        self.__load_model()
        test_array = np.array([self.Glucose,self.BloodPressure,self.SkinThickness,self.Insulin,self.BMI,
                          self.DiabetesPedigreeFunction,self.Age], ndmin=2)
        print(test_array)
        scaled_arr = self.scaler.transform(test_array)
        print(scaled_arr)
        prediction_1 = self.model.predict(test_array)[0]
        print(prediction_1)
        return prediction_1
        
        
