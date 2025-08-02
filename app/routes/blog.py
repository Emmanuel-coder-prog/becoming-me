from flask import Blueprint, render_template, abort
from app.models import BlogPost

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/blog/<int:post_id>')
def blog_detail(post_id):
    post = BlogPost.query.get_or_404(post_id)
    return render_template('blog_detail.html', post=post)
