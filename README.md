# 🌸 Iris Flower Classification App

A simple and elegant **Machine Learning Web App** built using **Streamlit** that predicts the species of an Iris flower — *Setosa*, *Versicolor*, or *Virginica* — based on sepal and petal measurements.

---

## 🪷 Project Overview
This project demonstrates how a **Random Forest Classifier** can classify Iris flowers using four simple features.  
It also includes a clean Streamlit UI for making live predictions from user input.

---

## 🌼 Dataset
- 📊 **Source:** Iris Dataset (`iris.csv`)
- 🧩 **Features:**
  - Sepal Length (cm)
  - Sepal Width (cm)
  - Petal Length (cm)
  - Petal Width (cm)
- 🎯 **Target Classes:**
  - Iris-setosa  
  - Iris-versicolor  
  - Iris-virginica

---

## 🧠 Model Details
- **Algorithm:** Random Forest Classifier 🌳  
- **Split:** 80% training / 20% testing  
- **Label Encoding:** Applied to species names  
- **Saved Models:**  
  - `model.pkl` (trained model)  
  - `label_encoder.pkl` (for decoding predictions)

---

## 📈 Model Performance
| Metric | Score |
|:-------|:------:|
| **Accuracy** | 🟢 **90%** |
| **Precision (avg)** | 0.93 |
| **Recall (avg)** | 0.89 |
| **F1-Score (avg)** | 0.89 |

---

## 📊 Classification Report
