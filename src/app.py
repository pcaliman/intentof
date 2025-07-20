from flask import Flask, request, render_template, jsonify
from pickle import load
import joblib
import pandas as pd
from datetime import datetime

app = Flask(__name__)

modelos = joblib.load("./src/modelos_unicos.pkl")

@app.route("/", methods = ["GET", "POST"])
def index():

    pred_class = None
    if request.method == "POST":
        y_pred=1234
        pred_class=int(y_pred)
    else:
        pred_class = None
    
    return render_template("index.html", prediction = pred_class)
