from flask import Flask, render_template, request, redirect, url_for, flash

def create_app():
    app = Flask(__name__)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)