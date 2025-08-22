from flask import Flask, render_template, redirect, request, url_for
from . import route_dp
from ..models import create_user, update_user, delete_user, list_users, User, db

@route_dp.route('/')
def homepage():
    return render_template('base.html')

@route_dp.route('/users', methods=['GET'])
def users_request():
    users = list_users()
    return render_template('users.html', users=users)

@route_dp.route('/creating', methods=['GET', 'POST'])
def creating_user():
    email_exists = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        age = request.form.get('age')
        age = int(age)
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            email_exists = f'Este email já está registrado.'
            return render_template('user_creation.html', email_exists=email_exists)
        create_user(name, email, age)
        return redirect(url_for('routes.users_request'))
    return render_template('user_creation.html', email_exists=email_exists)

@route_dp.route('/deleting/<int:user_id>', methods=['POST'])
def deleting_user(user_id):
    delete_user(user_id)
    return redirect(url_for('routes.users_request'))

@route_dp.route('/updating<int:user_id>', methods=['GET', 'POST'])
def updating_user(user_id):
    user = User.query.get(user_id)
    if not user:
        error = f'Erro ao encontrar {user_id}'
        return redirect(url_for('routes.users_request', error=error))
    if request.method == 'POST':
        new_name = request.form.get('new_name')
        new_email = request.form.get('new_email')
        new_age = request.form.get('new_age')
        update_user(user_id, new_name, new_email, new_age)
        return redirect(url_for('routes.users_request'))
    return render_template('updating_user.html', user=user)
