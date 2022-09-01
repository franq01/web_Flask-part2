
from flask import Flask, render_template, request
from  flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField


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

class LoginForm(FlaskForm):
    username = EmailField ('Username')
    password = StringField ('Password')
    submit = SubmitField ('Login')


    ###### rutas de login ####
@app.route('/auth/login')
def login ():
    form = LoginForm()
    return render_template('auth/login.html', form=form)

@app.route('/auth/registrer')
def register():
     return render_template('auth/registrer.html')


############ aqui tengo el er
@app.route('/welcome', methods=['GET' , 'POST'])

def welcome():
    email = request.form['mail']
    password = request.form['password']
    access = {'email': email, 'password':password}

    return render_template('admin/index.html', user_access=access )


@app.errorhandler(404)
def page_error_not_found(e):
    return render_template('error/404.html')



if __name__ == '__main__':
    app.run(debug=True)
