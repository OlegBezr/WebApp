from flask import Flask, render_template
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__) #create instance of the app

info = ''
model = ''

@app.route("/") #path to our app after IP->Port
def index(): #function for app to call
	predict_param = info.values.tolist()[0][1:]
	prediction = np.squeeze(model.predict([predict_param]).round(1))
	return render_template("index.html", prediction = prediction)

if __name__ == '__main__':
    model = joblib.load('regr.pkl')
    #I save data for prediction in csv file
    info = pd.read_csv("info.csv")
    app.run(debug=True)