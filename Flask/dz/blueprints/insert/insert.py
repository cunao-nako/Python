from flask import render_template, request, Blueprint, session, url_for, redirect, current_app

from connect_manager import UseDatabase, ConnectionErrors, SQLErrors

insert = Blueprint('insert', __name__, template_folder='templates')


def show_schedule(cursor):
    SQL = "SELECT idschedule, classroom, date, idcommision, isused FROM schedule WHERE isused = 0;"
    cursor.execute(SQL)
    result = []
    schema = ['ID', 'Аудитория', 'Дата проведения', 'Номер коммссии']
    for blank in cursor.fetchall():
        result.append(dict(zip(schema, blank)))
    result = list(filter(lambda item: str(item['ID']) not in session['draft'].keys(), result))
    return result


def insert_to_table(cursor, date, idcommission, classroom):
    cursor.execute('SELECT MAX(idschedule) FROM schedule;')
    idschedule = cursor.fetchall()[0][0]
    if idschedule is None:
        idschedule = 0
    idschedule += 1
    print(idschedule)
    SQL = "INSERT INTO `dz`.`schedule` (`idschedule`, `classroom`, `date`, `idcommision`, `isused`)" \
          f"VALUES({idschedule}, '{classroom}', '{date}', '{idcommission}', '0');"
    cursor.execute(SQL)


def delete_from_schedule(cursor, idschedule):
    SQL = f"DELETE FROM schedule WHERE idschedule={idschedule}"
    cursor.execute(SQL)
    return


@insert.route('/', methods=['POST', 'GET'])
def insert_page():
    if 'user' in session:
        if request.path in session['user']['path']:
            if 'delete' in request.form:
                idschedule = request.form.get('idschedule')
                with UseDatabase(current_app.config['dbconfig']) as cursor:
                    print(idschedule)
                    delete_from_schedule(cursor, idschedule)
                    schedule = show_schedule(cursor)
                    return render_template('insert.html', schedule=schedule)
            else:
                try:
                    with UseDatabase(current_app.config['dbconfig']) as cursor:
                        schedule = show_schedule(cursor)
                        return render_template('insert.html', schedule=schedule)
                except ConnectionErrors:
                    return render_template('error.html', message='Проблема с подключением к БД')
                except SQLErrors:
                    return render_template('error.html', message='Ошибка исполнения запроса')
        else:
            message = {'title': 'Ошибка',
                       'message': f"Доступ к странице для вашей роли \'{session['user']['role']}\' запрещен!"}
            return render_template('error.html', message=message)
    else:
        return redirect(url_for("login.login_page"))


@insert.route('/add/', methods=['POST', 'GET'])
def insert_page_adder():
    if 'user' in session:
        if request.path in session['user']['path']:
            if 'insert' in request.form:
                print('insert нажали')
                classroom = request.form.get('classroom')
                idcommission = request.form.get('commission')
                date = request.form.get('date')
                try:
                    with UseDatabase(current_app.config['dbconfig']) as cursor:
                        insert_to_table(cursor, date, idcommission, classroom)
                        return redirect(url_for('insert.insert_page'))
                except ConnectionErrors:
                    return render_template('error.html', message='Проблема с подключением к БД')
                except SQLErrors:
                    return render_template('error.html', message='Ошибка исполнения запроса')
            else:
                return render_template('add.html')
        else:
            message = {'title': 'Ошибка',
                       'message': f"Доступ к странице для вашей роли \'{session['user']['role']}\' запрещен!"}
            return render_template('error.html', message=message)
    else:
        return redirect(url_for('login.login_page'))
