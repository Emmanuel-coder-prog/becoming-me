import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, session
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from app import db
from app.models import Profile, Order
from datetime import datetime
from werkzeug.exceptions import RequestEntityTooLarge
from app.routes.team import team_bp



main = Blueprint("main", __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route("/")
def home():
    return render_template("index.html", now=datetime.utcnow())

@main.route("/about")
def about():
    return render_template("about.html")
@main.route('/contact', methods=['GET', 'POST'])
def contact():
    success = False
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        success = True
        flash("Your message was sent successfully!", "success") 
        return redirect(url_for('main.contact'))  
    return render_template('contact.html', success=success)


@main.route("/resume")
def resume():
    return render_template("resume.html")

@main.route("/services")
def services():
    return render_template("services.html")

@main.route("/services/graphic-design")
def graphic_design():
    return render_template("services/design-branding.html")


@main.route("/services/training")
def training():
    return render_template("training.html")

@main.route('/company')
def company():
    return render_template('company.html')

@main.route('/career')
def career():
    return render_template('career.html')

@main.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@main.route('/blog')
def blog():
    return render_template('blog.html')

@main.route('/dashboard')
@login_required
def dashboard():
    user = current_user
    orders = Order.query.filter_by(user_id=user.id).order_by(Order.created_at.desc()).all()
    return render_template('dashboard.html', user=user, orders=orders)

@main.route('/edit-profile')
@login_required
def edit_profile():
    return render_template('edit_profile.html')

@main.route('/upload-profile-image', methods=['POST'])
@login_required
def upload_profile_image():
    if 'profile_image' not in request.files:
        flash('No file part', 'error')
        return redirect(url_for('main.dashboard'))

    file = request.files['profile_image']

    if file.filename == '':
        flash('No selected file', 'error')
        return redirect(url_for('main.dashboard'))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)

        profile = current_user.profile
        if not profile:
            profile = Profile(user_id=current_user.id)
            db.session.add(profile)
        profile.image_url = f"/static/uploads/profile_pics/{filename}"
        db.session.commit()

        flash('Profile image uploaded successfully!', 'success')
        return redirect(url_for('main.dashboard'))

    flash('Invalid file type', 'error')
    return redirect(url_for('main.dashboard'))

@main.route('/orders')
@login_required
def orders():
    return render_template('orders.html')

@main.route('/services/web-development')
def web_development():
    return render_template('services/web-development.html')

@main.route('/services/design-branding')
def design_branding():
    return render_template('services/design-branding.html')

@main.route('/services/cybersecurity')
def cybersecurity():
    return render_template('services/cybersecurity.html')

@main.route('/custom-order', methods=['POST'])
def custom_order():
    service_name = request.form.get('service')
    name = request.form.get('name')
    email = request.form.get ('email')
    details = request.form.get('details')

    if not current_user.is_authenticated:
        session['pending_order'] = {
            'service_name': service_name,
            'name': name,
            'email': email,
            'details': details
        }
        flash("Please log in to complete your custom order.")
        return redirect(url_for('login'))

    order = Order(
        service_name=service_name,
        price=0.0,
        status='pending',
        user_id=current_user.id,
        created_at=datetime.utcnow()
    )
    db.session.add(order)
    db.session.commit()
    flash("Your custom order has been submitted successfully.")
    return redirect(url_for('main.dashboard'))


@main.route('/order-package', methods=['POST'])
@login_required
def order_package():
    tier = request.form.get('tier')
    price = float(request.form.get('price'))
    base_service = request.form.get('service_name')  

    service_name = f"{base_service} – {tier}"

    order = Order(
        service_name=service_name,
        price=price,
        status='pending',
        user_id=current_user.id,
        created_at=datetime.utcnow()
    )

    db.session.add(order)
    db.session.commit()

    flash(f"You successfully ordered the {tier} package for {base_service}.", "success")
    return redirect(url_for('main.dashboard'))



@main.route("/blog/3")
def blog_cybersecurity_mindset():
    return render_template("blog_detail_cybersecurity_mindset.html")


@main.route("/blog/1")
def blog_fullstack_choice():
    return render_template("blog_detail_fullstack.html")

@main.route("/blog/2")
def blog_design_thinking():
    return render_template("blog_detail_design_thinking.html")


@main.errorhandler(413)
def request_entity_too_large(error):
    flash("File too large. Maximum allowed size is 2 MB.")
    return redirect(request.referrer or url_for('dashboard'))


@main.route('/team/<name>')
def team_profile(name):
    return render_template(f'team/{name}.html')


