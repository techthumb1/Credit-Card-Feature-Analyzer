# --> Web App/app.py

from flask import Flask, render_template, request, jsonify, redirect, url_for
import numpy as np
import pandas as pd
import pickle
import os

model = os.path.join(os.path.dirname(__file__), "stat_models", "classification_model.pkl")
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/features')
def features():
    return render_template('layout.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    #return jsonify(output)
    print('Final features: ', final_features)
    print('Prediction: ', prediction)

    output = round(prediction[0], 2)
    print('Output: ', output)

    if output == 1:
        return render_template('layout.html', prediction_text='The transaction is fraudulent')
    else:
        return render_template('layout.html', prediction_text='The transaction is not fraudulent')


@app.route('/prediction', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    #return jsonify(output)
    print('Final features: ', final_features)
    print('Prediction: ', prediction)

    output = round(prediction[0], 2)
    print('Output: ', output)

    if output == 1:
        return render_template('prediction.html', prediction_text='The transaction is fraudulent')
    else:
        return render_template('prediction.html', prediction_text='The transaction is not fraudulent')


if __name__ == '__main__':
    app.run(debug=True)
