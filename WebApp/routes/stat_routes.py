# web_app/routes/stat_routes.py

from flask import Blueprint, request, jsonify, render_template
from sklearn.linear_model import LogisticRegression # for example
from web_app.models import User, Tweet

stat_routes = Blueprint("stat_routes", __name__)

@stats_routes.route("/predict", methods=["POST"])
def predict():
    print("PREDICT ROUTE...")
    print("FORM DATA:", dict(request.form))

    customer_a = request.form["customer_a"]
    customer_b = request.form["customer_b"]
    fraud_text = request.form["fraud_text"]

#    print("-----------------")
#    print("FETCHING TWEETS FROM THE DATABASE...")
#   
#    #TODO
#
#    print("-----------------")
#    print("TRAINING THE MODEL...")
#    
#    classifier = LogisticRegression()
#    # TODO: classifier.fit(___________, ___________)
#
#    print("-----------------")
#    print("MAKING A PREDICTION...")
    # result_a = classifier.predict([customer_a].embedding])
    # result_b = classifier.predict([customer_b].embedding])    
#
#    # TODO
    
    return render_template("prediction_results.html", 
        screen_name_a=customer_a, 
        screen_name_b=customer_b, 
        tweet_text=tweet_text, 
        result_a=result_a, 
        result_b=result_b,
        fraud_text=fraud_text,
        customer_most_likely="TODO",# result[0] 
    )