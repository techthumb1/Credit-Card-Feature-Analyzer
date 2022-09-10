# Create a Procfile with Gunicorn and Flask
web: gunicorn app:app --log-file - --log-level debug --reload
# web: python app.py
# This tells Heroku to run the app.py file when the app is started.
# The app.py file should contain the following code:
# import os 
# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def hello():
#     return 'Hello World!'
# if __name__ == '__main__':
#     app.run(debug=True, host='5001')

