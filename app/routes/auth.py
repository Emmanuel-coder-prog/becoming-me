

from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from app.forms import LoginForm 
from app.models import User
from app import db
 

team_bp = Blueprint('team', __name__)
auth_bp = Blueprint("auth", __name__)
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)

            
            pending = session.pop('pending_order', None)
            if pending:
                order = Order(
                    service_name=pending['service_name'],
                    price=0.0,
                    status='pending',
                    user_id=current_user.id,
                    created_at=datetime.utcnow()
                )
                db.session.add(order)
                db.session.commit()
                flash("Custom order placed after login.", "success")

            return redirect(url_for('main.dashboard'))


        flash("Invalid credentials", "danger")

    return render_template('auth/login.html', form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You’ve been logged out.", "info")
    return redirect(url_for("main.home"))


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

       
        if User.query.filter((User.email == email) | (User.username == username)).first():
            flash("Email or username already exists", "warning")
        else:
            user = User(username=username, email=email)
            user.set_password(password) 
            db.session.add(user)
            db.session.commit()         
            flash("Account created successfully!", "success")
            return redirect(url_for("auth.login"))

    return render_template('auth/register.html')


@auth_bp.route('/team/emmanuel')
def team_emmanuel():
    return render_template('team/emmanuel.html')


@team_bp.route('/team/benjamin')
def team_benjamin():
    return render_template('team/benjamin.html')







