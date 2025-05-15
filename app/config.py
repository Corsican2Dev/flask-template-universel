import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-key")
    DEBUG = os.getenv("FLASK_DEBUG", "1") == "1"
    API_URL = os.getenv("API_URL", "https://api.example.com")
