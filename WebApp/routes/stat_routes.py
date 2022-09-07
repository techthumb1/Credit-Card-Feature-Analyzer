# web_app/routes/stat_routes.py

from flask import Blueprint, request, render_template
from sklearn.linear_model import LogisticRegression 

stat_routes = Blueprint("stat_routes", __name__)

@stat_routes.route("/predict", methods=["POST"])
def predict():
    print("PREDICT ROUTE...")
    print("FORM DATA:", dict(request.form))

    customer_a = request.form["customer_a"]
    customer_b = request.form["customer_b"]
    fraud_text = request.form["fraud_text"]

    print("-----------------")
    print("TRAINING THE MODEL...")
    X, y = MODEL_FILEPATH(return_X_y=True)
    
    classifier = LogisticRegression()
    classifier.fit(X, y)

    print("-----------------")
    print("MAKING A PREDICTION...")
    result_a = classifier.predict([customer_a].embedding)
    result_b = classifier.predict([customer_b].embedding)    
    print("RESULT:", result_a, result_b)
    
    return render_template("prediction_results.html", 
        screen_name_a=customer_a, 
        screen_name_b=customer_b, 
        result_a=result_a, 
        result_b=result_b,
        fraud_text=fraud_text,
        customer_most_likely= result_a[0] 
    )