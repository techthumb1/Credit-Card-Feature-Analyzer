# Path: WebApp/routes/home_routes.py

from flask import Blueprint, render_template, request, redirect, url_for

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    return render_template('prediction_form.html')


@home_routes.route("/welocme")
def welcome():
    return f"Credit Card Feature Analyzer"


@home_routes.route("/about")
def about():
    print('Visiting the about page')
    return "About me"
