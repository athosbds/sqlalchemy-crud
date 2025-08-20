from flask import Flask, render_template, redirect, request, url_for
from . import route_dp
from ..models import create_user, update_user, delete_user, list_users
from datetime import datetime

@route_dp.route('/')
def homepage():
    return render_template('base.html')

@route_dp.route('/users', methods=['GET'])
def users_request():
    users = list_users()
    return render_template('users.html', users=users)

@route_dp.route('/creating', methods=['GET', 'POST'])
def creating_user():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        birthday_str = request.form.get('birth-year')
        age = None
        try:
            birthday_year = int(birthday_str)  
            current_year = datetime.now().year
            age = current_year - birthday_year   
        except ValueError:
            return "Ano de nascimento inválido"
        create_user(name, email, age)
        return redirect(url_for('users_request'))
    return render_template('user_creation.html')

@route_dp.route('/deleting<int:user_id>', methods=['POST'])
def deleting_user(user_id):
    delete_user(user_id)
    return redirect(url_for('users_request'))