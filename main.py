from flask import Flask, url_for, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aboba_secret_key'

class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

#@app.route("/")
#def hello():
#    return "Пудж самый лучший мужчина в мире"

@app.route("/")
@app.route("/index")
def index():
    user = "20KIS3"
    return render_template('index.html', title="Home page", username=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)

@app.route("/success")
def succes():
    user = "20KIS3"
    return user + " МЕГАХОРОООООООООООООООООООООООООООООООООООООООООООООООООООООООШ!"

def image3():
    return f'''<img src="{url_for('static', filename='image/images.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''

if __name__ == '__main__':
    app.run()