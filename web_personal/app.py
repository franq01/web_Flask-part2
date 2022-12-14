########################## Import Flask & python #########################
import email
from multiprocessing import connection
from flask import Flask
########################### Import  APP ####################
from home.views import home_blueprint
from auth.views import auth_blueprint
from error_pages.handlers import error_pages
from projects.views import project_blueprint

from db.db_conection import get_conection


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['ENV']= 'developmen'



################ Apss #################
app.register_blueprint(home_blueprint)
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(error_pages)
app.register_blueprint(project_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
