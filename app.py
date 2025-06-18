from flask import Flask, render_template
from services.blog.app import create_app as create_blog_app, register_generators
from services.projects.app import create_app as create_projects_app
from services.cv.app import create_app as create_cv_app
import os

app = Flask(__name__)
app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_RELATIVE_URLS'] = True

# Create service apps
blog_app = create_blog_app()
projects_app = create_projects_app()
cv_app = create_cv_app()

# Register blueprints from services
app.register_blueprint(blog_app.blueprints['blog'])
app.register_blueprint(projects_app.blueprints['projects'])
app.register_blueprint(cv_app.blueprints['cv'])

@app.route('/')
def index():
    # Get recent posts from blog service
    posts = [p for p in blog_app.blueprints['blog'].pages if p.path.startswith('posts/')]
    posts.sort(key=lambda p: p.meta.get('date', ''), reverse=True)
    return render_template('index.html', posts=posts[:6])

if __name__ == '__main__':
    if os.environ.get('FLASK_ENV') == 'development':
        app.run(debug=True, port=5000)
    else:
        from flask_frozen import Freezer
        freezer = Freezer(app)
        # Register generators from blog service
        register_generators(freezer)
        freezer.freeze() 