from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    login_manager.login_view = 'auth.login'  

    from app.models import User  

    from app.routes.auth import auth_bp
    from app.routes.main import main  
    from app.routes.company import company_bp

    app.register_blueprint(company_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(main)  

    return app
