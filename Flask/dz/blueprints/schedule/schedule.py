from flask import render_template, request, Blueprint, session, url_for, current_app

from connect_manager import UseDatabase, ConnectionErrors, SQLErrors

schedule = Blueprint('schedule', __name__, template_folder='templates')


def get_projects(cursor):
    SQL = "SELECT idproject, topic, fio, surname FROM project JOIN student USING(idstudent)" \
          f"JOIN teacher USING(idteacher) WHERE idschedule is NULL AND idreport is NULL"
    cursor.execute(SQL)
    result = []
    schema = ['ID', 'Тема проекта', 'Фамилия студента', 'Фамилия преподавателя']
    for blank in cursor.fetchall():
        result.append(dict(zip(schema, blank)))
    result = list(filter(lambda item: str(item['ID']) not in session['draft'].keys(), result))
    return result


def show_schedule(cursor):
    SQL = "SELECT idschedule, classroom, date, idcommision, isused FROM schedule WHERE isused = 0;"
    cursor.execute(SQL)
    result = []
    schema = ['ID', 'Аудитория', 'Дата проведения', 'Номер коммссии']
    for blank in cursor.fetchall():
        result.append(dict(zip(schema, blank)))
    result = list(filter(lambda item: str(item['ID']) not in session['draft'].values(), result))
    return result


def submit_draft(cursor, idproject=0):
    if idproject:
        SQL = f"UPDATE project SET idschedule={session['draft'][idproject]} WHERE idproject={idproject};"
        cursor.execute(SQL)
        SQL = f"UPDATE schedule SET isused = 1 WHERE idschedule={session['draft'][idproject]};"
        cursor.execute(SQL)
        session['draft'].pop(idproject)
    else:
        for idproject, idschedule in session['draft'].items():
            SQL = f"UPDATE project SET idschedule={idschedule} WHERE idproject={idproject};"
            cursor.execute(SQL)
            SQL = f"UPDATE schedule SET isused = 1 WHERE idschedule={idschedule};"
            cursor.execute(SQL)
            session['draft'] = {}
    return {'title': 'Сообщение', 'message': 'Черновик принят', 'redirect': '/schedule/'}


@schedule.route('/', methods=['POST', 'GET'])
def schedule_page():
    if 'user' in session:
        if request.path in session['user']['path']:
            session.modified = True
            if 'choose' in request.form:
                idproject = request.form.get('idproject')
                with UseDatabase(current_app.config['dbconfig']) as cursor:
                    catalog = show_schedule(cursor)
                return render_template('schedule.html', catalog=catalog, project_id=idproject)
            elif 'draft' in request.form:
                return render_template('draft.html', draft=session['draft'])
            elif 'enter' in request.form:
                idproject = request.form.get('idproject')
                idschedule = request.form.get('idschedule')
                session['draft'].update({idproject: idschedule})
                message = {'title': 'Сообщение', 'message': 'Запись добавлена в черновик', 'redirect': '/schedule/'}
                return render_template('error.html', message=message)
            elif 'insert' in request.form:
                with UseDatabase(current_app.config['dbconfig']) as cursor:
                    if request.form.get('idproject'):
                        message = submit_draft(cursor, request.form['idproject'])
                    else:
                        message = submit_draft(cursor)
                return render_template('error.html', message=message)
            elif 'clear' in request.form:
                if request.form.get('idproject'):
                    del session['draft'][request.form['idproject']]
                else:
                    session['draft'] = {}
                return render_template('draft.html', draft=session['draft'])
            else:
                try:
                    message = {'title': 'Ошибка'}
                    with UseDatabase(current_app.config['dbconfig']) as cursor:
                        projects = get_projects(cursor)
                        return render_template('catalog.html', projects=projects)
                except ConnectionErrors:
                    message.update({'message': 'Проблема с подключением к БД'})
                    return render_template('error.html', message=message)
                except SQLErrors:
                    message.update({'message': 'Ошибка исполнения запроса'})
                    return render_template('error.html', message=message)
        else:
            message = {'title': 'Ошибка', 'message': f"Доступ к странице для вашей роли '{session['user']['role']}' запрещен!"}
            return render_template('error.html', message=message)
    else:
        return render_template(url_for('login.login_page'))
