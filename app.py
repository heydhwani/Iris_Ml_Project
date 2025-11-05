from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load model and encoder
model = joblib.load("model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Iris ML API is running!"}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json  # Get JSON input

    features = np.array([[
        data["sepal_length"],
        data["sepal_width"],
        data["petal_length"],
        data["petal_width"]
    ]])

    prediction = model.predict(features)[0]
    decoded_prediction = label_encoder.inverse_transform([prediction])[0]

    return jsonify({"prediction": decoded_prediction})

if __name__ == "__main__":
    app.run(debug=True)
