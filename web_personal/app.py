

import email
from flask import Flask, redirect, render_template, request, url_for
from  flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, IntegerField, RadioField,SelectField
from wtforms.validators import DataRequired,Email


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


##### rutas public #######

@app.route('/')
def index():
    return render_template('public/index.html')

@app.route('/about')
def about():
    return render_template ('public/about.html')

@app.route('/contact')
def contact():
    return render_template ('public/contact.html')


@app.route('/portfolio')
def portfolio():
    return render_template ('public/portfolio.html')


    #################### Formularios de WTforms  #########################

    ############## Falta corregir email validator############

class LoginForm(FlaskForm):
    email = EmailField ('correo', validators=[DataRequired()])
    password = PasswordField ('Password', validators=[DataRequired()])
    submit = SubmitField ('Ingresar')


class RegisterForm(FlaskForm):
    name = StringField('Nombre')
    last_name = StringField('Apellidos')
    email = EmailField('correo')
    password = PasswordField('Contraseña')
    phone = IntegerField('Telefono')
    is_married = RadioField('Estado Civil', choices=[('True', 'Casado'),('False','Soltero')])
    gender = SelectField('Genero', choices=[('male','Masculino'), ('female','Femenino'), ('other','Otro')])
    submit = SubmitField('Registrar')


    ###### rutas de login ####
@app.route('/auth/login', methods=['GET','POST'])
def login ():
    form = LoginForm()
    if form.validate_on_submit():
       email = form.email.data
       password = form.password.data
      

       return render_template('admin/index.html', email=email )

    return render_template('auth/login.html', form=form)

@app.route('/auth/registrer')
def register():
    form = RegisterForm()
    return render_template('auth/registrer.html', form=form)






@app.errorhandler(404)
def page_error_not_found(e):
    return render_template('error/404.html')



if __name__ == '__main__':
    app.run(debug=True)
