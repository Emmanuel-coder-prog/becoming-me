

from flask import Blueprint, render_template

team_bp = Blueprint('team', __name__)

@team_bp.route('/team/benjamin')
def team_benjamin():
    return render_template('team/benjamin.html')
