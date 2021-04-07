import json
from flask import Flask, render_template, session, redirect, url_for

from blueprints.login.login import login
from blueprints.signin.signin import signin
from blueprints.queries.queries import queries
from blueprints.reports.reports import reports
from blueprints.schedule.schedule import schedule
from blueprints.insert.insert import insert

app = Flask(__name__, static_folder='static', template_folder='templates')
app.register_blueprint(login, url_prefix='/login/')
app.register_blueprint(signin, url_prefix='/signin/')
app.register_blueprint(queries, url_prefix='/queries/')
app.register_blueprint(reports, url_prefix='/reports/')
app.register_blueprint(schedule, url_prefix='/schedule/')
app.register_blueprint(insert, url_prefix='/insert/')

with open('data_files/dbconfig.json', 'r', encoding='utf-8') as file:
    app.config['dbconfig'] = json.load(file)

with open('data_files/menu_items.json', 'r', encoding='utf-8') as file:
    menu_items = json.load(file)

with open('data_files/secret_key.json', 'r', encoding='utf-8') as file:
    app.secret_key = json.load(file)['secret_key']


@app.route('/')
def main_menu():
    if 'user' in session:
        return render_template('index.html', menu=menu_items)
    else:
        return redirect(url_for('login.login_page'))


@app.route("/exit/")
def exit_page():
    session.pop('user', 'draft')
    return render_template('exit.html')


if __name__ == '__main__':
    app.run(debug=True)
