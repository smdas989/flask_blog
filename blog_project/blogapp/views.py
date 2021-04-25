from flask import flash, redirect, render_template, url_for
from blogapp import app
from flask.views import View
from flask.views import MethodView
from .forms import RegistrationForm, LoginForm
from blogapp.models import User, Post


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', title='Home')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        
        flash(f'Account created for {form.username}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data== 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, Please check username or password', 'danger')
    return render_template('login.html', title='Login', form=form)