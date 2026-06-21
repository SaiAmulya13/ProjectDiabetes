# Diabetes Prediction System

## 📌 Overview
This project predicts whether a person is diabetic or not using Machine Learning. The model is trained on diabetes data and deployed using Flask with a simple web interface.

## 🚀 Features
- Predicts diabetes based on patient details
- User-friendly HTML interface
- Machine Learning model using Random Forest
- Data preprocessing with imputer and scaler
- Flask backend for prediction

## 🛠 Technologies Used
- Python
- Flask
- Scikit-learn
- NumPy
- HTML/CSS
- Pickle

## 📂 Project Structure

```
ProjectDiabetes/
│── app.py
│── rf_model.pkl
│── scaler.pkl
│── imputer.pkl
│── requirements.txt
│── README.md
│── templates/
│    └── index.html
```

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/SaiAmulya13/ProjectDiabetes.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the application

```bash
python app.py
```

4. Open in browser

```
http://127.0.0.1:5000/
```

## 📊 Input Features
- Pregnancies
- Glucose Concentration
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

## 📈 Output
- Diabetic
- Not Diabetic

## 👩‍💻 Author
**Sai Amulya**