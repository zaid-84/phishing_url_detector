from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the trained model from phishing_model.pkl
with open('phishing_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Initialize Flask application
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the URL from the form
        url = request.form['url']

        # Make the prediction using the trained model
        prediction = model.predict([url])
        
        # Return the result as either phishing or safe
        if prediction[0] == 1:
            return render_template('index.html', prediction_text="This URL is Safe!")
        else:
            return render_template('index.html', prediction_text="This URL is Phishing!")

if __name__ == "__main__":
    app.run(debug=True)
