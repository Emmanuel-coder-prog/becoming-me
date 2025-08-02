

from flask import Blueprint, render_template
from flask_login import login_required

company_bp = Blueprint('company', __name__, template_folder='../templates')

@company_bp.route('/company')
@login_required
def company_page():
    team = [
        {"name": "Emmanuel Owusu Boakye", "role": "CEO & Lead Developer"},
        {"name": "Grace Mensah", "role": "UI/UX Designer"},
        {"name": "Benjamin Hotor", "role": "Cybersecurity Analyst"},
    ]
    return render_template('company.html', team=team)
