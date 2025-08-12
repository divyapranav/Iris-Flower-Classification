# app.py
from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load model & target names
with open("model.pkl", "rb") as f:
    model, target_names = pickle.load(f)

@app.route('/')
def index():
    return render_template('iris.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from form
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])

        # Prepare data
        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

        # Predict
        prediction = model.predict(features)[0]
        predicted_class = target_names[prediction]

        return jsonify({'prediction': predicted_class})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
