# Path: WebApp/routes/predict.py

import os
import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
os.environ['KMP_DUPLICATE_LIB_OK']='True'
#import lightgbm as lgb

# Load Model

# Save the model to disk
import pickle
clf_model = 'classification_model.sav'
pickle.dump(model, open(clf_model, 'wb'))


# Load the model
# Load the model from disk
loaded_model = pickle.load(open(clf_model, 'rb'))
result = loaded_model.score(X_test, y_test)
print(result)

# Return is fraud or not fraud
y_pred = loaded_model.predict(X_test)
print(y_pred)

# Return probability of fraud
y_pred_prob = loaded_model.predict_proba(X_test)[:,1]   
print(y_pred_prob)


def load_model():
    print("LOADING THE MODEL...")
    with open(loaded_model, "rb") as model_file:
        saved_model = pickle.load(model_file)
    return saved_model


if __name__== "__main__":

    train_and_save_model()

    clf = load_model()
    print("CLASSIFIER:", clf)

    X, y = clf(return_X_y=True)
    inputs = X[:2, :]
    print(type(inputs), inputs)

    result = clf.predict(inputs)
    print("RESULT:", result)

    plot_importance(clf)
    plt.show()


#model = pickle.load(open('classification_model.sav', 'rb'))
#
## Load Model
#filename = 'classification_model.sav'
#pickle.dump(model, open(filename, 'wb'))
#
## load the model from disk
#loaded_model = pickle.load(open(filename, 'rb'))
#result = loaded_model.score(X_test, Y_test)
#print(result)
#
## Predict the response for test dataset
#y_pred = loaded_model.predict(X_test)
#print(y_pred)
#model = pickle.load(open('cc_transaction.pkl', 'rb'))