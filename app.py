#!/usr/bin/env python
# coding: utf-8

from flask import Flask,render_template,request
import joblib
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict_title_Category',methods=['POST'])
def predict_expenses():
    return render_template('index.html', prediction_text='Hello to the Flask Application!')

if __name__ == "__main__":
    app.run(debug=True)
