from flask import Flask, render_template
import joblib
import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor

model = joblib.load("regr.pkl")
info = pd.read_csv("info.csv")

app = Flask(__name__) #create instance of the app

@app.route("/") #path to our app after IP->Port
def index(): #function for app to call
	predict_param = info.values.tolist()[0][1:]
	prediction = np.squeeze(model.predict([predict_param]).round(1))
	return render_template("index.html", prediction = prediction)

if __name__ == "__main__":
    #I save data for prediction in csv file
	app.run(debug=True)