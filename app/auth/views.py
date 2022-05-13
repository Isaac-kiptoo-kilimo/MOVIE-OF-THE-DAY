
from unicodedata import category
from flask import render_template,url_for,redirect,flash
from . import main
from .forms import RegistrationForm,LoginForm,PitchForm
from models import Pitch, User,Category
from app import db




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

