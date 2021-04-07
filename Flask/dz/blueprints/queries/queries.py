import json
from flask import render_template, request, Blueprint, current_app, session, redirect, url_for

from connect_manager import UseDatabase, ConnectionErrors, SQLErrors

queries = Blueprint('queries', __name__, template_folder='templates')

with open('data_files/requests.json', 'r', encoding='utf-8') as f:
    requests = json.load(f)

with open('data_files/queries_items.json', 'r', encoding='utf-8') as f:
    queries_list = json.load(f)


def simple_query(cursor, idquery):
    cursor.execute(requests[idquery]["query"])
    response = []
    schema = requests[idquery]["schema"].split(",")
    for item in cursor.fetchall():
        response.append(dict(zip(schema, item)))
    return response


@queries.route('/', methods=['GET'])
def queries_page():
    if 'user' in session:
        if request.path in session['user']['path']:
            if request.args.get("query"):
                idquery = int(request.args.get("query"))
                print(idquery)
                message = {'title': 'Ошибка', 'redirect': '/queries/'}
                try:
                    with UseDatabase(current_app.config['dbconfig']) as cursor:
                        result = simple_query(cursor, idquery)
                        if result:
                            return render_template('result.html', result=result, url='/queries/')
                        else:
                            message.update({'message': 'По данному запросу нет данных'})
                            return render_template('error.html', message=message)
                except ConnectionErrors:
                    message.update({'message': 'Проблема с подключением к Базе Данных'})
                    return render_template('error.html', message=message)
                except SQLErrors:
                    message.update({'message': 'Ошибка исполнения запроса'})
                    return render_template('error.html', message=message)
            else:
                return render_template('queries.html', queries=queries_list)
        else:
            message = {'title': 'Ошибка',
                       'message': f"Доступ к странице для вашей роли \'{session['user']['role']}\' запрещен!"}
            return render_template('error.html', message=message)
    else:
        return redirect(url_for('login.login_page'))
