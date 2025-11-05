import streamlit as st
import numpy as np
import joblib

# Load your trained model (replace with your file name)
model = joblib.load("model.pkl")

st.title("🌸 Iris Flower Classifier")
st.write("Enter the flower measurements below:")

# User inputs
sepal_length = st.number_input("Sepal Length (cm)", 0.0, 10.0, 5.1)
sepal_width  = st.number_input("Sepal Width (cm)", 0.0, 10.0, 3.5)
petal_length = st.number_input("Petal Length (cm)", 0.0, 10.0, 1.4)
petal_width  = st.number_input("Petal Width (cm)", 0.0, 10.0, 0.2)

if st.button("Predict"):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)[0]
    

    # Map numeric label to species name
    species_map = {
        0: "Iris-setosa 🌼",
        1: "Iris-versicolor 🌷",
        2: "Iris-virginica 🌹"
    }

    species_name = species_map.get(prediction, "Unknown")

    st.success(f"🌸 **Predicted Species:** {species_name}")
