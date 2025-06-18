from flask import Flask, Blueprint, render_template
import os

cv_bp = Blueprint('cv', __name__, url_prefix='/cv')

def create_app():
    app = Flask(__name__)
    app.config['FREEZER_DESTINATION'] = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'build/cv')
    app.config['FREEZER_RELATIVE_URLS'] = True

    app.register_blueprint(cv_bp)
    return app

@cv_bp.route('/')
def index():
    cv_data = {
        'name': 'Your Name',
        'title': 'Deep Learning Engineer',
        'contact': {
            'email': 'your.email@example.com',
            'github': 'https://github.com/yourusername',
            'linkedin': 'https://linkedin.com/in/yourusername'
        },
        'education': [
            {
                'degree': 'Master of Science in Computer Science',
                'school': 'University Name',
                'year': '2020-2022'
            }
        ],
        'experience': [
            {
                'title': 'Deep Learning Engineer',
                'company': 'Company Name',
                'period': '2022-Present',
                'description': 'Description of your role and achievements'
            }
        ],
        'skills': [
            'Python', 'TensorFlow', 'PyTorch', 'Deep Learning',
            'Machine Learning', 'Computer Vision', 'NLP'
        ]
    }
    return render_template('cv/index.html', cv=cv_data)

if __name__ == '__main__':
    app = create_app()
    if os.environ.get('FLASK_ENV') == 'development':
        app.run(debug=True, port=5003)
    else:
        from flask_frozen import Freezer
        freezer = Freezer(app)
        freezer.freeze() 