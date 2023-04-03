#!/usr/bin/env python
# coding: utf-8

from flask import Flask,render_template,request
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)
model = joblib.load(open('Sentiment.pkl', 'rb'))

df = pd.read_csv("C:\\Masters\\608\\OpinRankDatasetWithJudgments\\hotels\\Merged All cities CSV for model\\All_City_Merged.csv")
cols= ["Reviews","Name"]
df_final = df[cols]

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict_title_Category',methods=['POST'])
def predict_expenses():
    trxt = [str(x) for x in request.form.values()]
    prediction = model.predict(trxt)
    #print(Final_string)
    return render_template('index.html', prediction_text='{}'.format(prediction))
"""
def predict_expenses():
    #int_features = [int(x) for x in request.form.values()]
    #final_features = [np.array(int_features)]
    lst_ = [request.form.values()]
    prediction = model.predict(lst_)
    output = round(prediction)
    #return render_template('index.html', prediction_text='Predicted tile is in channel $ {}'.format(output))
    return render_template('index.html', prediction_text='Predicted tile is in channel $ {}'.format(output))
"""

if __name__ == "__main__":
    app.run(debug=True)