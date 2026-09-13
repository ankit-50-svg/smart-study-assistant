import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret-key")
    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "ai_study_assistant")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")
