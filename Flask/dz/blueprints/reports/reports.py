from flask import render_template, request, Blueprint, session, redirect, url_for, current_app

from connect_manager import UseDatabase, ConnectionErrors, SQLErrors

reports = Blueprint('reports', __name__, template_folder='templates')


def do_report(cursor, start, end):
    SQL = f"SELECT COUNT(*) FROM exam WHERE start='{start}' and end='{end}';"
    cursor.execute(SQL)
    if len(cursor.fetchall()):
        SQL = f"SELECT * FROM exam WHERE start='{start}' and end='{end}';"
        cursor.execute(SQL)
        result = []
        schema = ['ID', 'Фамилия', 'Средняя оценка', 'Общее число студентов', 'Начало промежутка', 'Конец промежутка']
        for blank in cursor.fetchall():
            result.append(dict(zip(schema, blank)))
        return result
    else:
        return None


@reports.route('/', methods=['GET'])
def reports_page():
    if 'user' in session:
        if request.path in session['user']['path']:
            return render_template('reports.html')
        else:
            message = {'title': 'Ошибка',
                       'message': f"Доступ к странице для вашей роли '{session['user']['role']}' запрещен!"}
            return render_template('error.html', message=message)
    else:
        return redirect(url_for('login.login_page'))


@reports.route('/report1/', methods=['POST', 'GET'])
def report1_page():
    if 'send' in request.form:
        start = request.form.get('date-start')
        end = request.form.get('date-end')
        message = {'title': 'Ошибка', 'redirect': '/reports/'}
        try:
            with UseDatabase(current_app.config['dbconfig']) as cursor:
                result = do_report(cursor, start, end)
            if result:
                return render_template('result.html', result=result, url='/reports/')
            else:
                message.update({'message': 'Нет данных для заданного промежутка'})
                return render_template('error.html', message=message)
        except ConnectionErrors:
            message.update({'message': 'Проблема с подключением к БД'})
            return render_template('error.html', message=message)
        except SQLErrors:
            message.update({'message': 'Ошибка исполнения запроса'})
            return render_template('error.html', message=message)
    else:
        return render_template('report1.html')
