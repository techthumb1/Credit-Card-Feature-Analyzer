from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    return f"Credit Card Feature Analyzer"

@home_routes.route("/about")
def about():
    print('Visiting the about page')
    return "About me"

# Path: WebApp/routes/home_routes.py