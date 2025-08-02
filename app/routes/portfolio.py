from flask import Blueprint, render_template

portfolio_bp = Blueprint("portfolio", __name__, url_prefix="/portfolio")

@portfolio_bp.route("/")
def portfolio_index():
    return render_template("portfolio/index.html")

@portfolio_bp.route("/<project_slug>")
def project_detail(project_slug):
    return render_template("portfolio/detail.html", slug=project_slug)
