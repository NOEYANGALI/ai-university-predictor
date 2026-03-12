# AI University Service Predictor

**CS50x Final Project — 2026**  
**Author: Noe Juan Yangali Ibarra**

---

## 📌 Project Description

A machine learning web application that predicts academic risk for university students and recommends the right support services. Built with Flask, scikit-learn, and Chart.js.

## 🎯 Features

- **AI Prediction**: Random Forest model (200 trees) trained on student behavioral data
- **Risk Assessment**: LOW / MEDIUM / HIGH classification with probability scores
- **Smart Recommendations**: Personalized university service suggestions
- **Analytics Dashboard**: Charts showing risk distribution, stress levels, GPA patterns
- **Session History**: Track all predictions in current session

## 🛠️ Tech Stack

- **Backend**: Python, Flask, Flask-Session
- **ML**: scikit-learn (RandomForestClassifier), pandas, numpy
- **Frontend**: HTML, CSS, JavaScript, Chart.js
- **Templates**: Jinja2

## 🚀 How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
flask run
```

Then visit `http://localhost:5000`

## 📊 Input Variables

| Variable | Description | Range |
|---|---|---|
| GPA | Grade Point Average | 0.0 – 4.0 |
| Attendance | Class attendance % | 0 – 100 |
| Library Usage | Monthly visits | 0 – 15 |
| Online Activity | Digital engagement | 0 – 10 |
| Stress Level | Self-reported (1=calm) | 1 – 10 |
| Sleep Hours | Nightly average | 3 – 10 |

## 📁 File Structure

```
ai_university_predictor/
├── app.py                  # Flask routes
├── model_ml.py             # ML model + prediction logic
├── students_dataset.csv    # Training data (50 students)
├── requirements.txt
├── templates/
│   ├── layout.html         # Base template
│   ├── index.html          # Homepage
│   ├── predict.html        # Input form
│   ├── result.html         # Prediction result
│   ├── dashboard.html      # Analytics dashboard
│   └── about.html          # About page
└── README.md
```

## 🧠 ML Model Details

- **Algorithm**: Random Forest Classifier
- **Trees**: 200 estimators
- **Validation**: 5-fold cross-validation
- **Target**: `needs_support` (binary: 0 = stable, 1 = at risk)
- **Accuracy**: ~95%

## 📽️ Video Demo
https://www.youtube.com/watch?v=6Qev1Khqnq8
---

*Built for CS50x 2026 — Harvard University*
