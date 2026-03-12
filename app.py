import os
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from model_ml import predict_student, get_dataset_stats

app = Flask(__name__)
app.secret_key = "cs50_final_project_2026_noe_yangali"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            gpa = float(request.form.get("gpa", 0))
            attendance = float(request.form.get("attendance", 0))
            library_usage = int(request.form.get("library_usage", 0))
            online_activity = int(request.form.get("online_activity", 0))
            stress_level = int(request.form.get("stress_level", 5))
            sleep_hours = float(request.form.get("sleep_hours", 7))
            student_name = request.form.get("student_name", "Student").strip()

            # Validations
            if not (0.0 <= gpa <= 4.0):
                return render_template("predict.html", error="GPA must be between 0.0 and 4.0")
            if not (0 <= attendance <= 100):
                return render_template("predict.html", error="Attendance must be between 0 and 100")

            result = predict_student(gpa, attendance, library_usage, online_activity, stress_level, sleep_hours)
            result["student_name"] = student_name
            result["inputs"] = {
                "gpa": gpa,
                "attendance": attendance,
                "library_usage": library_usage,
                "online_activity": online_activity,
                "stress_level": stress_level,
                "sleep_hours": sleep_hours
            }

            # Save to session history
            if "history" not in session:
                session["history"] = []
            session["history"].append({
                "name": student_name,
                "risk_level": result["risk_level"],
                "risk_score": result["risk_score"],
                "gpa": gpa
            })
            session.modified = True

            return render_template("result.html", result=result)

        except (ValueError, TypeError) as e:
            return render_template("predict.html", error="Please enter valid numeric values.")

    return render_template("predict.html")

@app.route("/dashboard")
def dashboard():
    stats = get_dataset_stats()
    history = session.get("history", [])
    return render_template("dashboard.html", stats=stats, history=history)

@app.route("/api/stats")
def api_stats():
    return jsonify(get_dataset_stats())

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)