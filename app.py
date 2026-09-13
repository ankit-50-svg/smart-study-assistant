from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("auth/login.html")

@app.route("/register")
def register():
    return render_template("auth/register.html")

@app.route("/dashboard")
def dashboard():
    return render_template("user/dashboard.html")

@app.route("/subjects")
def subjects():
    return render_template("subjects/subjects.html")

@app.route("/study-plan")
def study_plan():
    return render_template("study/study_plan.html")

@app.route("/ai-tutor")
def ai_tutor():
    return render_template("ai/ai_tutor.html")

@app.route("/notes")
def notes():
    return render_template("notes/notes.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz/quiz.html")

@app.route("/progress")
def progress():
    return render_template("progress/progress.html")

@app.route("/reminders")
def reminders():
    return render_template("reminders/reminders.html")

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
