from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.routes.team import team_bp





db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///becomingme_db.db'

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login' 

    from app.routes.main import main_bp
    from app.routes.auth import auth_bp  

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    app.register_blueprint(blog_bp)

    app.register_blueprint(team_bp)


    return app
