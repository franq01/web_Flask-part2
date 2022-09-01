
########### Import flask y python###############
from flask import render_template, Blueprint

from db.db_conection import get_conection
########### Iports WTF ##############3
from .forms import LoginForm, RegisterForm


auth_blueprint = Blueprint('auth', __name__)




   ###### rutas de login ####
@auth_blueprint.route('/login', methods=['GET','POST'])
def login ():
    form = LoginForm()
    if form.validate_on_submit():
       email = form.email.data
       password = form.password.data

       ####### TODO: consulta a la base de datos######
      

       return render_template('admin/index.html', email=email )

    return render_template('auth/login.html', form=form)

@auth_blueprint.route('/registrer')
def register():
    form = RegisterForm()


    ################### TODO: validar usuario ###########

    

    return render_template('auth/registrer.html', form=form)
