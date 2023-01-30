from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User,Note
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import login_user,logout_user,login_required,current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                if email == 'lalit@gmail.com':
                    flash('Logged in as admin', category='success')
                    login_user(user, remember = True)
                    return redirect(url_for('views.home'))
                else:
                    flash('Logged in successfully', category='success')
                    login_user(user, remember = True)
                    return redirect(url_for('views.home'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('User not found', category='error')
    return render_template('login.html' ,user = current_user)

@auth.route('/sign_up' , methods = ['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()


        if user:
            flash('Email already exists', category='error')
        elif len(email)<5:
            flash('Email must be longer than 4 characters', category='error')
        elif len(username)<2:
            flash('Name must be longer than 2 characters', category='error')
        elif password1!=password2:
            flash('Your passwords should match', category='error')
        elif len(password1)<6:
            flash('Password must be greater than 5 characters', category='error')
        else:
            new_user = User(email = email, username = username, password = generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember = True)
            flash('Sign up sucessful', category='success')
            return redirect(url_for('views.home'))


    return render_template('sign_up.html',user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))

@auth.route('/query')
@login_required
def query():
    dataa = Note.query.all()
    users = User.query.all()
    return render_template('query.html', user = current_user, users = users,dataa = dataa)