from flask import Blueprint,render_template
home_blueprint = Blueprint('', __name__)

##### rutas public #######

@home_blueprint.route('/')
def index():
    return render_template('public/index.html')

@home_blueprint.route('/about')
def about():
    return render_template ('public/about.html')

@home_blueprint.route('/contact')
def contact():
    return render_template ('public/contact.html')


@home_blueprint.route('/portfolio')
def portfolio():
    return render_template ('public/portfolio.html')
