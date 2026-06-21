from flask import Flask, render_template, request
import numpy as np
import pickle

# Load the model, scaler, and imputer
with open('rf_model.pkl', 'rb') as f:
    rf_model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('imputer.pkl', 'rb') as f:
    fill_zeros = pickle.load(f)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # ✅ UPDATED: now 10 fields
        field_names = [
            'num_preg',
            'glucose_conc',
            'diastolic_bp',
            'skin',
            'insulin',
            'bmi',
            'diab_pred',
            'age'
        ]

        # Get data from form
        form_data = {field: request.form[field] for field in field_names}

        # Convert to float
        features = [float(form_data[field]) for field in field_names]

        # Convert to numpy array
        input_array = np.asarray(features).reshape(1, -1)

        # Preprocess
        input_array = fill_zeros.transform(input_array)
        input_array = scaler.transform(input_array)

        # Predict
        prediction = rf_model.predict(input_array)
        result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"

        return render_template(
            'index.html',
            prediction_text=f'Prediction: {result}',
            form_data=form_data
        )

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')


if __name__ == "__main__":
    app.run(debug=True)