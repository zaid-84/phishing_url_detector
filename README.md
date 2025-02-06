# phishing_url_detector

This project aims to build a Phishing URL Detector using machine learning. The model classifies URLs as either "Phishing" or "Safe" based on their characteristics. The project uses a trained machine learning model to detect phishing links, which are often used for fraudulent activities such as identity theft and data breaches.

Project Overview
The Phishing URL Detector provides a user-friendly web application to detect phishing URLs. The application is built using the Flask framework for the backend, where the trained machine learning model is used to make predictions. The frontend is designed with HTML and CSS, offering a simple interface where users can enter a URL to check whether it is phishing or safe.

Features:
Phishing URL Detection: The application uses a machine learning model to classify URLs as phishing or safe.
Simple Web Interface: Users can input a URL into a form, and the application will return the result.
Model Integration: The machine learning model is integrated into the Flask app to make real-time predictions.
Requirements
To run this project locally, you need the following dependencies:

Python 3.x
Flask
scikit-learn
pandas
numpy
pickle
