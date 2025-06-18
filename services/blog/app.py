from flask import Flask, Blueprint, render_template, abort
from flask_flatpages import FlatPages
from flask_frozen import Freezer
import os

blog_bp = Blueprint('blog', __name__, url_prefix='/blog')
pages = None
freezer = None

def create_app():
    app = Flask(__name__)
    app.config['FLATPAGES_ROOT'] = os.path.join(os.path.dirname(__file__), 'content')
    app.config['FLATPAGES_EXTENSION'] = '.md'
    app.config['FLATPAGES_MARKDOWN_EXTENSIONS'] = ['codehilite', 'fenced_code', 'tables', 'toc']
    app.config['FREEZER_DESTINATION'] = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'build/blog')
    app.config['FREEZER_RELATIVE_URLS'] = True

    global pages, freezer
    pages = FlatPages(app)
    freezer = Freezer(app)

    app.register_blueprint(blog_bp)
    return app

@blog_bp.route('/')
def index():
    posts = [p for p in pages if p.path.startswith('posts/')]
    posts.sort(key=lambda p: p.meta.get('date', ''), reverse=True)
    return render_template('blog/index.html', posts=posts)

@blog_bp.route('/<path:path>/')
def post(path):
    post = pages.get_or_404(f'posts/{path}')
    return render_template('blog/post.html', post=post)

def register_generators(freezer):
    @freezer.register_generator
    def post_generator():
        for page in pages:
            if page.path.startswith('posts/'):
                yield {'path': page.path[6:]}

if __name__ == '__main__':
    app = create_app()
    if os.environ.get('FLASK_ENV') == 'development':
        app.run(debug=True, port=5001)
    else:
        freezer.freeze() 