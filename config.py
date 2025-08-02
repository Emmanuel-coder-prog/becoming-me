import os

class Config:
    
    SECRET_KEY = os.getenv("SECRET_KEY", "devkey")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:hello@localhost/becomingme_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app', 'static', 'uploads')  
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024  
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
