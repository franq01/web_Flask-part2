from  flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, IntegerField, RadioField,SelectField
from wtforms.validators import DataRequired,Email




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