# --> Web App/app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the data from the POST request.
        data = request.form.to_dict()
        print(data)
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
