from flask import Flask, request, render_template, session, redirect

app = Flask(__name__)

app.secret_key = 'NNNN'


@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main.html')


@app.route('/about/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')



if __name__ == '__main__':
    app.run()
