#!/usr/bin/python
# -*- coding: utf-8 -*-
# app/home/views.py

from flask import render_template, request, jsonify
from flask import *
import os
import pandas as pd
from . import home
from . forms import File_form
from werkzeug.utils import secure_filename
import yagmail


# @home.route('/')
# def homepage():
#     """
#     Render the homepage template on the / route
#     """

#     return render_template('home/index.html', title='Welcome')


@home.route('/', methods=['GET', 'POST'])
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """

    form = File_form()
    if form.validate_on_submit():
        option = form.option.data
        filename = secure_filename(form.file.data.filename)
        form.file.data.save('app/files/' + filename)

        yagmail.register(form.email.data, form.password.data)
        yag = yagmail.SMTP(form.email.data)

        file_path = 'app/files/' + filename
        file = pd.read_excel(file_path)

        mails = []
        email_subject = 'Yagmail Test'
        contents = ' This is a Test mail'
        

        if option=='Mail to departments':
            department = pd.read_excel('app/dept.xlsx')

            file.sort_values('Dept', axis=0, ascending=True, inplace=True, na_position='last')

            dept_mail = {}
            for (index, row) in department.iterrows():
                if row['Dept'] in dept_mail.keys():
                    dept_mail[row['Dept']].append(row['mail'])
                else:
                    dept_mail[row['Dept']] = []
                    dept_mail[row['Dept']].append(row['mail'])

            depts = [] + ['Default']
            for (index, row) in file.iterrows():
                if row['Dept'] not in depts:
                    depts.append(row['Dept'])
            
            for i in depts:
                if i in dept_mail.keys():
                    mails.extend(dept_mail[i])
            mails = ['avulapatin.cs18@rvce.edu.in']
            yag.send(to=mails,cc='niranjan.prep@gmail.com', subject=email_subject, contents=contents, attachments=[file_path])
        else:
            for (index, row) in file.iterrows():
                mail.append(row['Dept'])
            yag.send(to=mails,cc='niranjan.prep@gmail.com', subject=email_subject, contents=contents, attachments=[file_path])
        
        os.remove(file_path)
        return redirect(url_for('home.sheet'))
    return render_template('home/dashboard.html', title='Dashboard',
                           form=form)


@home.route('/sheet', methods=['GET', 'POST'])
def sheet():
    return render_template('home/sheet.html', title='upload success')
