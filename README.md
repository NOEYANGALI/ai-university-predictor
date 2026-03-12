# AI University Service Predictor

**CS50x Final Project — 2026**
**Author: Noe Juan Yangali Ibarra**

## Video Demo
https://www.youtube.com/watch?v=6Qev1Khqnq8

## Description

AI University Service Predictor is a web application built with Flask and Python that uses machine learning to predict whether a university student is at academic risk and recommends the appropriate university support services. The system analyzes six key behavioral and academic variables: GPA, class attendance percentage, monthly library visits, online activity score, stress level, and average sleep hours per night.

The core of the application is a Random Forest Classifier with 200 decision trees trained on a dataset of 50 university students. The model achieves approximately 95% accuracy with 5-fold cross-validation, making it reliable for real-world academic advising scenarios.

When a student's data is entered into the prediction form, the model calculates a risk score from 0 to 100 and classifies the student as LOW, MEDIUM, or HIGH risk. Based on this classification and the specific input values, the system generates personalized recommendations for university services such as the Academic Tutoring Center, Psychological Counseling Services, Student Wellness Program, Library and Learning Resources, and the Digital Learning Center.

The application includes five pages: a homepage explaining the system, a prediction form with sliders and input fields, a results page showing the risk assessment with a visual ring chart and probability breakdown, an analytics dashboard with four Chart.js charts showing risk distribution and stress levels across the dataset, and an about page documenting the technology and methodology used.

The project was built using Flask for the backend routing and session management, Jinja2 for HTML templating, scikit-learn for the machine learning model, pandas for data processing, and Chart.js for the interactive dashboard visualizations. The design uses a dark theme with CSS variables and Google Fonts for a professional appearance.
