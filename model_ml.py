import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "students_dataset.csv")

# Load and prepare data
data = pd.read_csv(DATA_PATH)

FEATURES = ['gpa', 'attendance', 'library_usage', 'online_activity', 'stress_level', 'sleep_hours']
TARGET = 'needs_support'

X = data[FEATURES]
y = data[TARGET]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Train Random Forest (primary model)
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=8,
    min_samples_split=3,
    random_state=42,
    class_weight='balanced'
)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
cv_scores = cross_val_score(model, X, y, cv=5)

# Feature importance
feature_importance = dict(zip(FEATURES, model.feature_importances_.tolist()))


def predict_student(gpa, attendance, library_usage, online_activity, stress_level, sleep_hours):
    """
    Predict if a student needs academic support.
    Returns: dict with prediction, probability, risk_level, recommendations
    """
    input_data = [[gpa, attendance, library_usage, online_activity, stress_level, sleep_hours]]
    
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]
    
    risk_score = probability[1] * 100  # probability of needing support
    
    if risk_score >= 70:
        risk_level = "HIGH"
        risk_color = "#ef4444"
    elif risk_score >= 40:
        risk_level = "MEDIUM"
        risk_color = "#f59e0b"
    else:
        risk_level = "LOW"
        risk_color = "#10b981"
    
    # Generate personalized recommendations
    recommendations = []
    
    if gpa < 2.5:
        recommendations.append({
            "icon": "📚",
            "service": "Academic Tutoring Center",
            "reason": "Your GPA indicates you may benefit from additional academic support",
            "priority": "HIGH"
        })
    
    if attendance < 75:
        recommendations.append({
            "icon": "🎯",
            "service": "Student Engagement Office",
            "reason": "Attendance below 75% significantly impacts academic performance",
            "priority": "HIGH"
        })
    
    if stress_level >= 7:
        recommendations.append({
            "icon": "🧘",
            "service": "Psychological Counseling Services",
            "reason": "High stress levels detected — mental health support is available",
            "priority": "HIGH"
        })
    
    if sleep_hours < 6:
        recommendations.append({
            "icon": "💤",
            "service": "Student Wellness Program",
            "reason": "Sleep deprivation affects cognitive performance and memory retention",
            "priority": "MEDIUM"
        })
    
    if library_usage < 4:
        recommendations.append({
            "icon": "🏛️",
            "service": "Library & Learning Resources",
            "reason": "Increased library usage correlates with better academic outcomes",
            "priority": "MEDIUM"
        })
    
    if online_activity < 4:
        recommendations.append({
            "icon": "💻",
            "service": "Digital Learning Center",
            "reason": "Boost engagement with online platforms and virtual study tools",
            "priority": "LOW"
        })
    
    if not recommendations:
        recommendations.append({
            "icon": "⭐",
            "service": "Excellence Scholarship Program",
            "reason": "You're performing excellently — consider applying for academic awards",
            "priority": "LOW"
        })
    
    # Academic profile analysis
    strengths = []
    areas_to_improve = []
    
    if gpa >= 3.5: strengths.append("Outstanding GPA")
    elif gpa >= 3.0: strengths.append("Good academic standing")
    
    if attendance >= 90: strengths.append("Excellent attendance")
    elif attendance >= 80: strengths.append("Good attendance")
    
    if stress_level <= 3: strengths.append("Low stress levels")
    if sleep_hours >= 7: strengths.append("Healthy sleep patterns")
    if library_usage >= 8: strengths.append("Active library engagement")
    
    if gpa < 2.5: areas_to_improve.append("Academic performance")
    if attendance < 75: areas_to_improve.append("Class attendance")
    if stress_level >= 7: areas_to_improve.append("Stress management")
    if sleep_hours < 6: areas_to_improve.append("Sleep habits")
    
    return {
        "prediction": int(prediction),
        "needs_support": bool(prediction == 1),
        "risk_score": round(risk_score, 1),
        "risk_level": risk_level,
        "risk_color": risk_color,
        "stable_probability": round(probability[0] * 100, 1),
        "support_probability": round(probability[1] * 100, 1),
        "recommendations": recommendations,
        "strengths": strengths,
        "areas_to_improve": areas_to_improve,
        "model_accuracy": round(accuracy * 100, 1),
        "cv_accuracy": round(cv_scores.mean() * 100, 1)
    }


def get_dataset_stats():
    """Return statistics about the dataset for the dashboard."""
    at_risk = int(data['needs_support'].sum())
    stable = int(len(data) - at_risk)
    
    stress_low = int((data['stress_level'] <= 3).sum())
    stress_med = int(((data['stress_level'] > 3) & (data['stress_level'] <= 6)).sum())
    stress_high = int((data['stress_level'] > 6).sum())
    
    avg_gpa = round(float(data['gpa'].mean()), 2)
    avg_attendance = round(float(data['attendance'].mean()), 1)
    avg_sleep = round(float(data['sleep_hours'].mean()), 1)
    
    return {
        "total_students": len(data),
        "at_risk": at_risk,
        "stable": stable,
        "at_risk_pct": round(at_risk / len(data) * 100, 1),
        "stress_low": stress_low,
        "stress_med": stress_med,
        "stress_high": stress_high,
        "avg_gpa": avg_gpa,
        "avg_attendance": avg_attendance,
        "avg_sleep": avg_sleep,
        "model_accuracy": round(accuracy * 100, 1),
        "feature_importance": feature_importance,
        "gpa_distribution": data['gpa'].tolist(),
        "attendance_distribution": data['attendance'].tolist()
    }
