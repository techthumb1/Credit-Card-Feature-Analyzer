# 

import os
import pickle
import pandas as pd
os.environ['KMP_DUPLICATE_LIB_OK']='True'
import lightgbm as lgb
from lightgbm import plot_importance

# Load Model
#MODEL_FILEPATH = os.path.join(os.path.dirname(__file__), "stat_models", "classification_model.pkl")
#
##def train_and_save_model():
##    print("TRAINING THE MODEL...")
##    X, y = MODEL_FILEPATH(return_X_y=True)
##    classifier = LogisticRegression() # for example
##    classifier.fit(X, y)
##
##    print("SAVING THE MODEL...")
##    with open(MODEL_FILEPATH, "wb") as model_file:
##        pickle.dump(classifier, model_file)
##
##    return classifier
#
#def load_model():
#    print("LOADING THE MODEL...")
#    with open(MODEL_FILEPATH, "rb") as model_file:
#        saved_model = pickle.load(model_file)
#    return saved_model
#
#
#if __name__== "__main__":
#
#    #train_and_save_model()
#
#    clf = load_model()
#    print("CLASSIFIER:", clf)
#
#    X, y = cct1(return_X_y=True)
#    inputs = X[:2, :]
#    print(type(inputs), inputs)
#
#    result = clf.predict(inputs)
#    print("RESULT:", result)
#
#    plot_importance(clf)
#    plt.show()


model = pickle.load(open('finalized_model.sav', 'rb'))

# Load Model
filename = 'classification_model.sav'
pickle.dump(model, open(filename, 'wb'))

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, Y_test)
print(result)

# Predict the response for test dataset
y_pred = loaded_model.predict(X_test)
print(y_pred)