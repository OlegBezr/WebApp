from flask import Flask, render_template
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__) #create instance of the app

@app.route("/") #path to our app after IP->Port
def index(): #function for app to call
	return render_template("index.html", prediction = prediction)

if __name__ == "__main__":
    #I save data for prediction in csv file
	model = joblib.load("regr.pkl")
	info = pd.read_csv("info.csv")
	predict_param = info.values.tolist()[0][1:]
	prediction = np.squeeze(model.predict([predict_param]).round(1))
	app.run(debug=True)