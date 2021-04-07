from flask import Blueprint, render_template, session, request, current_app, redirect, url_for

from connect_manager import UseDatabase

signin = Blueprint('signin', __name__, template_folder='templates')


def check_login(cursor, login):
    SQL = f'SELECT login FROM user WHERE login = "{login}"'
    cursor.execute(SQL)
    return cursor.fetchall()


def do_signin(cursor, login, password, role):
    SQL = 'SELECT MAX(iduser) FROM user'
    cursor.execute(SQL)
    iduser = cursor.fetchall()[0][0]
    if iduser is None:
        iduser = 0
    iduser += 1
    if len(check_login(cursor, login)):
        return {'title': 'Ошибка', 'message': 'Данный логин уже занят', 'redirect': '/signin/'}
    else:
        SQL = "INSERT INTO user (iduser, login, password, idrole)" \
              f"VALUES ({iduser}, '{login}', '{password}', {role});"
        cursor.execute(SQL)
        return {'title': 'Сообщение', 'message': 'Регистрация прошла успешно, теперь авторизируйтесь!'}


@signin.route('/', methods=['GET', 'POST'])
def signin_page():
    if 'signin' in request.form:
        login = request.form.get('login')
        password = request.form.get('password')
        role = request.form.get('role')
        with UseDatabase(current_app.config['dbconfig']) as cursor:
            message = do_signin(cursor, login, password, role)
        return render_template('error.html', message=message)
    if 'back' in request.form:
        return redirect(url_for('login.login_page'))
    else:
        return render_template('signin.html')
