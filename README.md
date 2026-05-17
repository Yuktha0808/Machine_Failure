# Machine Failure Prediction System

An AI-powered predictive maintenance web application built using Flask and Machine Learning that predicts machine failures, identifies failure types, and detects which machine parameters exceeded safe limits.

---

## Features

- Predicts machine failure using Machine Learning
- Identifies exact failure type
- Detects parameters causing failure
- Displays safe threshold limits
- Modern Flask web interface
- Background image UI
- Real-time prediction system
- Random Forest Classifier model

---

## Failure Types Supported

- Tool Wear Failure (TWF)
- Heat Dissipation Failure (HDF)
- Power Failure (PWF)
- Overstrain Failure (OSF)
- Random Failure (RNF)
- No Failure

---

## Tech Stack

### Frontend
- HTML
- CSS

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- Random Forest Classifier
- Pandas
- NumPy

---

## Project Structure

```plaintext
Machine_failure/
│
├── app.py
├── machine_failure_prediction.py
│
├── dataset/
│   └── machine_failure.csv
│
├── model/
│   └── machine_failure_model.joblib
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── images/
│       └── back.jpg
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Machine_failure.git
```

### Move Into Project Folder

```bash
cd Machine_failure
```

### Install Requirements

```bash
pip install -r requirements.txt
```

---

## Train Model

Run:

```bash
python machine_failure_prediction.py
```

This generates:

```plaintext
model/machine_failure_model.joblib
```

---

## Run Flask Application

```bash
python app.py
```

---

## Open in Browser

```plaintext
http://127.0.0.1:5000
```

---

## Input Parameters

The system accepts:

- Air Temperature
- Process Temperature
- Rotational Speed
- Torque
- Tool Wear

---

## Example Output

### Healthy Machine

- Machine is Healthy
- Failure Type: No Failure
- All parameters within safe limits

### Failed Machine

- Machine Failure Detected
- Failure Type: Heat Dissipation Failure
- Displays exceeded parameters

---

## Future Enhancements

- Real-time IoT sensor integration
- Dashboard analytics
- Live monitoring
- Failure probability graphs
- Downloadable reports
- Cloud deployment
- Database integration

---

## Dataset

Machine Predictive Maintenance Dataset used for training the ML model.

---

## Author

Developed by ALURI YUKTHA

---

## License

This project is for educational and learning purposes.
