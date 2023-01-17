import os
import pickle

import pandas as pd
from flask import Flask, request, jsonify
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Load the model
model_path = "models/model.pkl"
model = pickle.load(open(model_path, 'rb'))

@app.route("/predict", methods=["POST"])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([[np.array(data['exp'])]])
    # Take the first value of prediction
    output = prediction[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')























import os
import pickle
import warnings

import pandas as pd
from lightgbm import LGBMClassifier, plot_importance, LGBMRegressor
from sklearn.externals import joblib
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from flask import Flask, request, render_template, redirect, url_for, flash, jsonify

app = Flask(__name__)

# Load the model
model_path = "models/classification_model.pkl"
model = joblib.load(open(model_path, "rb"))

# Ignore warnings
warnings.filterwarnings("ignore", category=UserWarning)

class SilentRegressor(LGBMRegressor):
    def fit(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=UserWarning)
            return super().fit(*args, verbose=False, **kwargs)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Read in the transaction data
    cct1 = pd.read_csv("/Users/jasonrobinson/Documents/Data-Engineering-Credit-Card-Transactions/transactions.csv")

    # Drop unnecessary columns
    cct1 = cct1.drop(["Merchant State", "Errors?"], axis=1)

    # Fill missing values and extract relevant features
    cct1["Zip"] = cct1["Zip"].fillna(0)
    cct1["Amount"] = cct1["Amount"].apply(lambda value: float(value.split("$")[1]))
    cct1["Hour"] = cct1["Time"].apply(lambda value: int(value.split(":")[0]))
    cct1["Minutes"] = cct1["Time"].apply(lambda value: int(value.split(":")[1]))
    cct1.drop(["Time"], axis=1, inplace=True)

    # Convert columns to categorical data types
    cct1["Merchant Name"] = cct1["Merchant Name"].astype("object")
    cct1["Card"] = cct1["Card"].astype("object")
    cct1["Use Chip"] = cct1["Use Chip"].astype("object")
    cct1["MCC"] = cct1["MCC"].astype("object")
    cct1["Zip"] = cct1["Zip"].astype("object")
    for col in cct1.columns:
        col_type = cct1[col].dtype
        if col_type == "object" or col_type.name == "category":
            cct1[col] = cct1[col].astype("category")

    # Extract target variable and feature matrix
    y = cct1["Is Fraud?"].apply(lambda value: 1 if value == "Yes" else 0)
    X = cct1.drop(["Is Fraud?"], axis=1)

    
