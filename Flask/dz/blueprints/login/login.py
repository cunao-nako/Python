from flask import Blueprint, render_template, session, request, current_app, redirect, url_for

from connect_manager import UseDatabase

login = Blueprint('login', __name__, template_folder='templates')


def do_login(cursor, login, password):
    SQL = "SELECT login, role, path FROM user JOIN role USING(idrole) JOIN privilege USING(idrole)" \
          f"WHERE login = '{login}' and password = '{password}';"
    cursor.execute(SQL)
    result = cursor.fetchall()
    session['user'] = {'login': result[0][0], 'role': result[0][1], 'path': []}
    for tuples in result:
        session['user']['path'].append(tuples[2])
    session['draft'] = {}
    print(session['user'])


@login.route('/', methods=['GET', 'POST'])
def login_page():
    if 'signin' in request.form:
        return redirect(url_for('signin.signin_page'))
    if 'login' in request.form:
        users_login = request.form.get('login')
        password = request.form.get('password')
        try:
            with UseDatabase(current_app.config['dbconfig']) as cursor:
                do_login(cursor, users_login, password)
            return redirect(url_for('main_menu'))
        except IndexError:
            message = {'title': 'Ошибка', 'message': 'Введён неверный логин или пароль', 'redirect': '/login/'}
            return render_template('error.html', message=message)
    else:
        return render_template('login.html')
