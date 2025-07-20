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

def formatear_fecha(fecha_str):
    dt = datetime.strptime(fecha_str, "%Y-%m-%d")
    return dt.strftime("%Y-%m-%dT00:00:00-0400")


@app.route("/autocomplete/modelos")
def autocomplete_modelos():
    q = request.args.get("q", "").lower()
    sugerencias = [m for m in modelos if q in m.lower()][:10]
    return jsonify(sugerencias)

@app.route("/autocomplete/fabricantes")
def autocomplete_fabricantes():
    q = request.args.get("q", "").lower()
    sugerencias = [f for f in fabricantes if q in f.lower()][:10]
    return jsonify(sugerencias)

@app.route('/autocomplete/estados')
def autocomplete_estados():
    q = request.args.get('q', '').lower()
    sugerencias = [estado for estado in estados if q in estado.lower()]
    return jsonify(sugerencias)

@app.route("/", methods = ["GET", "POST"])
def index():

    pred_class = None
    if request.method == "POST":
        y_pred=1234
        pred_class=int(y_pred)
    else:
        pred_class = None
    
    return render_template("index.html", prediction = pred_class)
