#!/usr/bin/env python
# coding: utf-8

from flask import Flask,render_template,request
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)
model = joblib.load(open('Sentiment.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict_title_Category',methods=['POST'])
def predict_expenses():
    trxt = [str(x) for x in request.form.values()]
    prediction = model.predict(trxt)
    #print(Final_string)
    return render_template('index.html', prediction_text='Hello to the Flask Application!')

if __name__ == "__main__":
    app.run(debug=True)
