# Path: WebApp/routes/predict.py

# Load Model
model = pickle.load(open('cc_transaction.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the data from the POST request.
        data = request.form.to_dict()
        print(data)
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
    