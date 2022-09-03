from flask import Blueprint, jsonify, request, render_template #, flash, redirect

feature_routes = Blueprint("feature_routes", __name__)

@feature_routes.route("/features.json")
def list_features():
    features = [
        {"id": 1, "index": "Minutes"},
        {"id": 2, "index": "Hour"},
        {"id": 3, "index": "Amount"},
    ]
    return jsonify(features)

@feature_routes.route("/features")
def list_features_for_features():
    # Top 3 features of importance
    features = [
        {"id": 1, "index": "Minutes"},
        {"id": 2, "index": "Hour"},
        {"id": 3, "index": "Amount"},
    ]
    return render_template("features.html", message="Top 3 Features of Importance", features=features)

@feature_routes.route("/features/new")
def new_feature():
    return render_template("new_feature.html")

@feature_routes.route("/features/create", methods=["POST"])
def create_feature():
    print("FORM DATA:", dict(request.form))
    # todo: store in database
    return jsonify({
        "message": "FEATURE CREATED SUCCESSFULLY",
        "feature": dict(request.form)
    })
    #flash(f"features '{new_feature.title}' created successfully!", "success")
    #return redirect(f"/features")