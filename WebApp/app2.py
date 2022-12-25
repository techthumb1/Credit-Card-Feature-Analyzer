import os
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, jsonify
import pickle


app = Flask(__name__, template_folder='templates')  
app.config('EXPLAIN_TEMPLATE_LOADING') = True
model = pickle.load(open('model1.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))

@app.route('/results',methods=['POST'])
def results():
    
        '''
        For rendering results on HTML GUI
        '''
        data = request.get_json(force=True)
        prediction = model.predict([np.array(list(data.values()))])
    
        output = prediction[0]
        return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
    