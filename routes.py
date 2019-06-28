from flask import Flask, render_template

app = Flask(__name__) #create instance of the app

@app.route("/") #path to our app after IP->Port
def index(): #function for app to call
	return render_template("index.html")

if __name__ == "__main__":
	app.run(debug = True)
