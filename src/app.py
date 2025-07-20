from flask import Flask, request, render_template, jsonify
from pickle import load
import joblib
import pandas as pd
from datetime import datetime

app = Flask(__name__)

modelos = joblib.load("./src/modelos_unicos.pkl")
fabricantes = joblib.load("./src/Fabricantes_unicos.pkl")
estados = joblib.load("./src/State_unicos.pkl")

preprocessor = joblib.load("./models/preprocessor.pkl")
scaler = joblib.load("./models/scaler.pkl")
modelopredictor = joblib.load("./models/modelo_random_forest_Omega10.pkl")



@app.route("/", methods = ["GET", "POST"])
def index():

    pred_class = None
    if request.method == "POST":
        y_pred=1234
        pred_class=int(y_pred)
    else:
        pred_class = None
    
    return render_template("index.html", prediction = pred_class)
