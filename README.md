# ❤️ Stroke Risk Predictor (KNN Model)

A Machine Learning powered **Stroke Risk Prediction Web App** built using **Streamlit** and **K-Nearest Neighbors (KNN)**.
The application predicts the **risk of heart disease / stroke** based on user health parameters and provides instant results.

---

🌐 Live Demo

https://stroke-risk--predictor.streamlit.app/

---

## 📌 Features

* Clean & Professional UI
* Real-time Risk Prediction
* K-Nearest Neighbors (KNN) Model
* Probability-based Risk Score
* Interactive Sliders & Inputs
* Instant Health Risk Analysis

---

## 🧠 Machine Learning Model

* Algorithm: **K-Nearest Neighbors (KNN)**
* Preprocessing: **StandardScaler**
* Model Files:

  * `knn_model.pkl`
  * `scaler.pkl`
  * `columns.pkl`

---

## 📊 Input Parameters

The model uses the following health indicators:

* Age
* Sex
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Max Heart Rate
* ST Depression (Oldpeak)
* Chest Pain Type
* Resting ECG
* Exercise Induced Angina
* ST Slope

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Scikit-learn
* Pandas
* NumPy
* Joblib

---

## 📁 Project Structure

```
stroke-risk-predictor
│
├── stroke-risk-predictor
│   ├── app.py
│   ├── knn_model.pkl
│   ├── scaler.pkl
│   ├── columns.pkl
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```
git clone https://github.com/shubham-kumar145/stroke-risk-predictor.git
```

Navigate to project folder

```
cd stroke-risk-predictor
```

Install dependencies

```
pip install -r requirements.txt
```

Run the app

```
streamlit run stroke-risk-predictor/app.py
```

---

## 📈 Output

* Low Risk Prediction
* High Risk Prediction
* Probability Score
* Risk Breakdown

---

## ⚠️ Disclaimer

This application is for **educational purposes only** and should **not replace professional medical advice**.

---

## 👨‍💻 Author

**Shubham Kumar**
B.Tech ECE — BIT Mesra
Machine Learning & Full-Stack Developer

GitHub:
https://github.com/shubham-kumar145

---

## ⭐ If you like this project

Give it a ⭐ on GitHub
