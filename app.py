from flask import Flask, render_template, request
import numpy as np
import joblib
import os

# Create Flask app FIRST
app = Flask(__name__)

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'machine_failure_model.joblib')

model = joblib.load(MODEL_PATH)

# Failure thresholds
THRESHOLDS = {
    "Air Temperature": 310,
    "Process Temperature": 315,
    "Rotational Speed": 2500,
    "Torque": 60,
    "Tool Wear": 200
}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    try:
        air_temp = float(request.form['air_temp'])
        process_temp = float(request.form['process_temp'])
        rot_speed = float(request.form['rot_speed'])
        torque = float(request.form['torque'])
        tool_wear = float(request.form['tool_wear'])

        features = np.array([[
            air_temp,
            process_temp,
            rot_speed,
            torque,
            tool_wear
        ]])

        prediction = model.predict(features)[0]

        exceeded = []

        if air_temp > THRESHOLDS['Air Temperature']:
            exceeded.append(
                f"Air Temperature exceeded safe limit ({THRESHOLDS['Air Temperature']} K)"
            )

        if process_temp > THRESHOLDS['Process Temperature']:
            exceeded.append(
                f"Process Temperature exceeded safe limit ({THRESHOLDS['Process Temperature']} K)"
            )

        if rot_speed > THRESHOLDS['Rotational Speed']:
            exceeded.append(
                f"Rotational Speed exceeded safe limit ({THRESHOLDS['Rotational Speed']} rpm)"
            )

        if torque > THRESHOLDS['Torque']:
            exceeded.append(
                f"Torque exceeded safe limit ({THRESHOLDS['Torque']} Nm)"
            )

        if tool_wear > THRESHOLDS['Tool Wear']:
            exceeded.append(
                f"Tool Wear exceeded safe limit ({THRESHOLDS['Tool Wear']} min)"
            )

        if prediction == 'No Failure':
            status = 'Machine is Healthy'
        else:
            status = 'Machine Failure Detected'

        return render_template(
            'result.html',
            prediction=prediction,
            status=status,
            exceeded=exceeded
        )

    except Exception as e:
        return f"Error: {e}"


if __name__ == '__main__':
    app.run(debug=True)