# app/auth/views.py

from flask import flash, redirect, render_template, url_for

from . import auth
from . forms import Form


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """
    form = Form()
    if form.validate_on_submit() and form.email.data == 'niranjan' and form.password.data == 'password':
        return redirect(url_for('home.dashboard'))
    # else:
    #     flash('Invalid email or password.')
   
    return render_template('auth/login.html', form=form, title='Login')


