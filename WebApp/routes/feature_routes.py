from flask import Blueprint, jsonify, request, render_template #, flash, redirect

feature_routes = Blueprint("feature_routes", __name__)

@feature_routes.route("/features.json")
def list_features():
    features = [
        {"id": 1, "title": "Feature 1"},
        {"id": 2, "title": "Feature 2"},
        {"id": 3, "title": "Feature 3"},
    ]
    return jsonify(features)

@feature_routes.route("/features")
def list_features_for_features():
    features = [
        {"id": 1, "title": "Feature 1"},
        {"id": 2, "title": "Feature 2"},
        {"id": 3, "title": "Feature 3"},
    ]
    return render_template("features.html", message="Features of Importance", features=features)

@feature_routes.route("/features/new")
def new_feature():
    return render_template("new_feature.html")

@feature_routes.route("/features/create", methods=["POST"])
def create_feature():
    print("FORM DATA:", dict(request.form))
    # todo: store in database
    return jsonify({
        "message": "FEATURE CREATED OK (TODO)",
        "feature": dict(request.form)
    })
    #flash(f"features '{new_feature.title}' created successfully!", "success")
    #return redirect(f"/features")