from flask import Flask, Blueprint, render_template
import os

projects_bp = Blueprint('projects', __name__, url_prefix='/projects')

def create_app():
    app = Flask(__name__)
    app.config['FREEZER_DESTINATION'] = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'build/projects')
    app.config['FREEZER_RELATIVE_URLS'] = True

    app.register_blueprint(projects_bp)
    return app

@projects_bp.route('/')
def index():
    projects = [
        {
            'title': 'Project 1',
            'description': 'Description of project 1',
            'technologies': ['Python', 'Flask', 'React'],
            'github_url': 'https://github.com/username/project1'
        },
        {
            'title': 'Project 2',
            'description': 'Description of project 2',
            'technologies': ['Python', 'TensorFlow', 'Docker'],
            'github_url': 'https://github.com/username/project2'
        }
    ]
    return render_template('projects/index.html', projects=projects)

if __name__ == '__main__':
    app = create_app()
    if os.environ.get('FLASK_ENV') == 'development':
        app.run(debug=True, port=5002)
    else:
        from flask_frozen import Freezer
        freezer = Freezer(app)
        freezer.freeze() 