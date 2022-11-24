from flask import Flask, render_template, request, redirect, url_for, flash
import numpy as np
import pickle
import os
import pandas as pd
os.environ['KMP_DUPLICATE_LIB_OK']='True'
import lightgbm as lgb
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from lightgbm import plot_importance
from sklearn.metrics import confusion_matrix
import pickle

class SilentRegressor(lgb.LGBMRegressor):
    def fit(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=UserWarning)
            return super().fit(*args, verbose=False, **kwargs)

import warnings
warnings.filterwarnings("ignore", category=UserWarning)


app = Flask(__name__)

model = os.path.join(os.path.dirname(__file__), "classification_model.pkl")


with open(model, 'rb') as f:
    model = pickle.load(f)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET','POST'])
def prediction_results():
    cct1 = pd.read_csv('/Users/jasonrobinson/Documents/Data-Engineering-Credit-Card-Transactions/transactions.csv')

    cct1 = cct1.drop(['Merchant State','Errors?'], axis=1)

    cct1['Zip'] = cct1['Zip'].fillna(0)
    cct1['Amount'] = cct1['Amount'].apply(lambda value: float(value.split("$")[1]))
    cct1['Hour'] = cct1['Time'].apply(lambda value: int(value.split(":")[0]))
    cct1['Minutes'] = cct1['Time'].apply(lambda value: int(value.split(":")[1]))
    
    cct1.drop(['Time'], axis=1, inplace=True)

    cct1['Merchant Name'] = cct1['Merchant Name'].astype("object")
    cct1['Card'] = cct1['Card'].astype("object")
    cct1['Use Chip'] = cct1['Use Chip'].astype("object")
    cct1['MCC'] = cct1['MCC'].astype("object")
    cct1['Zip'] = cct1['Zip'].astype("object")

    for col in cct1.columns:
        col_type = cct1[col].dtype
        if col_type == 'object' or col_type.name == 'category':
            cct1[col] = cct1[col].astype('category')
    
    y = cct1['Is Fraud?'].apply(lambda value: 1 if value == 'Yes' else 0)
    #y = cct1['Is Fraud?']
    X = cct1.drop(['Is Fraud?'],axis=1)

    categorical_column_names = []
    categorical_cols = []
    for idx,col in enumerate(X.columns):
        col_type = X[col].dtype
        if col_type == 'object' or col_type.name == 'category':
            categorical_column_names.append(col)
            categorical_cols.append(idx)

    categorical_column_names.append("Zip")
    categorical_column_names.append("MCC")
    categorical_column_names.append("Card")
    categorical_column_names.append("Merchant Name")

    categorical_names = {}
    for feature in categorical_column_names:
        le = sklearn.preprocessing.LabelEncoder()
        le.fit(X.loc[:, feature])
        X.loc[:, feature] = le.transform(X.loc[:, feature])
        categorical_names[feature] = le.classes_

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0, stratify=y)

    model = lgb.LGBMClassifier()
    model.fit(X_train, y_train,
              feature_name='auto',
              categorical_feature=categorical_column_names,
              eval_set=[(X_test, y_test)],
              eval_metric='auc',
              early_stopping_rounds=5)

    # Change string to float (change up above)
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))
    
    return render_template('results.html', y_pred=y_pred)



if __name__ == '__main__':
    app.run(debug=True)

