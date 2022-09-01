
########### Import flask y python###############

from flask import render_template, Blueprint, redirect, url_for

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

@auth_blueprint.route('/registrer', methods=['GET','POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
      name= form.name.data
      last_name = form.last_name.data
      email =form.email.data
      password = form.password.data
      phone = form.phone.data
      is_married = form.is_married.data
      gender = form.gender.data


     
      conn = get_conection()
      with conn.cursor() as cursor:
         sql ="INSERT INTO users (name, last_name, email, password, phone, is_married, gender) "
         sql += f"VALUES ('{name}', '{last_name}', '{email}', '{password}', '{phone}', '{is_married}', '{gender}')"
         cursor.execute(sql)
         conn.commit()
         return redirect (url_for ('auth.login'))
      

    

    return render_template('auth/registrer.html', form=form)
