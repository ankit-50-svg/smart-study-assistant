#  AI Smart Study Assistant

An intelligent and personalized study management web application built with **Python, Flask, MongoDB, HTML, CSS, and JavaScript**.

The AI Smart Study Assistant helps students organize their studies, manage subjects and notes, create study plans, generate quizzes, analyze performance, and receive personalized learning recommendations.

##  Live Demo : https://smart-study-assistant-six.vercel.app/

##  About The Project

**AI Smart Study Assistant** is a student-focused web application designed to make studying more organized, personalized, and efficient.

The system provides multiple tools in one platform, including:

- 📚 Subject management
- 📝 Notes management
- 📄 PDF notes upload and summarization
- 🤖 AI Tutor
- 🧠 AI-powered study planning
- ❓ Quiz generation
- 📊 Performance analysis
- 🎯 Personalized recommendations
- 📈 Progress tracking
- ⏰ Study reminders
- 👤 Student registration and login
- 📊 Student dashboard

The project is developed as a **Python-based academic/portfolio project**.

---

##  Features

###  User Authentication
- Student registration
- Student login
- Secure password handling
- User session management

###  Student Dashboard
- Overview of study activities
- Study progress
- Subjects
- Notes
- Quizzes
- Reminders
- Study plans

###  Subject Management
- Add subjects
- View subjects
- Manage subject details
- Organize learning topics

###  Notes Management
- Create and manage study notes
- Upload PDF notes
- Read uploaded documents
- Generate summaries

###  AI Tutor
- Interactive AI learning assistant
- Ask study-related questions
- Get explanations
- Personalized learning assistance

###  AI Study Planner
- Create personalized study plans
- Organize study sessions
- Daily study planning
- Manage study goals

###  AI Quiz Generator
- Generate quizzes
- Start quizzes
- Submit answers
- View quiz results
- Track quiz performance

###  Performance Analysis
- Track student performance
- Analyze quiz results
- Monitor learning progress
- Identify areas that need improvement

###  Personalized Recommendations
- Learning recommendations
- Study suggestions
- Personalized improvement guidance

###  Study Reminders
- Create study reminders
- Manage reminders
- Track upcoming study activities

##  Technologies Used

### Backend
- Python
- Flask
- MongoDB
- PyMongo

### Frontend
- HTML5
- CSS3
- JavaScript

### AI & Data Processing
- Scikit-learn
- Requests
- PyMuPDF

### Database
- MongoDB

### Environment
- Python Virtual Environment
- `.env` configuration

##  Project Architecture

```text
AI-SMART-STUDY-ASSISTANT/
│
├── app.py
├── config.py
├── requirements.txt
├── .env.example
├── .gitignore
│
├── ai/
│   ├── __init__.py
│   ├── ai_assistant.py
│   ├── summarizer.py
│   ├── quiz_generator.py
│   ├── study_planner.py
│   ├── recommendation_engine.py
│   └── performance_analyzer.py
│
├── routes/
│   ├── __init__.py
│   ├── auth_routes.py
│   ├── dashboard_routes.py
│   ├── subject_routes.py
│   ├── note_routes.py
│   ├── ai_routes.py
│   ├── quiz_routes.py
│   ├── study_plan_routes.py
│   ├── progress_routes.py
│   └── reminder_routes.py
│
├── models/
│   ├── __init__.py
│   ├── user_model.py
│   ├── subject_model.py
│   ├── note_model.py
│   ├── quiz_model.py
│   ├── study_plan_model.py
│   ├── progress_model.py
│   └── reminder_model.py
│
├── utils/
│   ├── __init__.py
│   ├── auth.py
│   ├── helpers.py
│   ├── pdf_reader.py
│   └── validators.py
│
├── templates/
│   ├── index.html
│   ├── base.html
│   │
│   ├── auth/
│   │   ├── login.html
│   │   └── register.html
│   │
│   ├── user/
│   │   └── dashboard.html
│   │
│   ├── ai/
│   │   ├── ai_tutor.html
│   │   └── recommendations.html
│   │
│   ├── notes/
│   │   ├── notes.html
│   │   ├── upload.html
│   │   └── summary.html
│   │
│   ├── quiz/
│   │   ├── quiz.html
│   │   ├── start_quiz.html
│   │   └── result.html
│   │
│   ├── study/
│   │   ├── study_plan.html
│   │   ├── create_plan.html
│   │   └── daily_plan.html
│   │
│   ├── subjects/
│   │   ├── subjects.html
│   │   ├── add_subject.html
│   │   └── subject_detail.html
│   │
│   ├── reminders/
│   │   ├── reminders.html
│   │   └── add_reminder.html
│   │
│   └── progress/
│       └── progress.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   ├── main.js
│   │   ├── dashboard.js
│   │   ├── ai_tutor.js
│   │   ├── quiz.js
│   │   ├── study_plan.js
│   │   └── reminders.js
│   │
│   └── images/
│
├── uploads/
│   └── .gitkeep
│
└── tests/
    ├── test_ai.py
    ├── test_auth.py
    └── test_quiz.py
