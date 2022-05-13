
from unicodedata import category
from flask import render_template,url_for,redirect,flash,request
from . import main
from .forms import RegistrationForm,LoginForm,PitchForm
from models import Pitch, User,Category
from app import db
from . import auth
from flask_login import login_user,logout_user,login_required


@main.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    user_exist=User.query.filter_by(email=form.email.data).first() 
    if form.validate_on_submit() and user_exist is None: 
   
        user = User(username=form.username.data, email=form.email.data,
                password=form.password.data)

        print(form.username)
        db.session.add(user)
        db.session.commit()
        
        flash('Yaaaay! Thanks for registering!')

        return redirect(url_for('main.login'))
    flash('Username is taken')
    print(form.username.data,form.email.data,form.password.data,form.confirm_password.data)
    return render_template('register.html',title='register',form=form)

#diana

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "movie of the day login"
    return render_template('auth/login.html',login_form = login_form,title=title)
                           
                           
#logout

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

