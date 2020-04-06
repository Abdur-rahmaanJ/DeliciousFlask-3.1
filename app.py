from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'abcd'

@app.route('/test')
def route_test():
    return 'test ok'


@app.route('/greet/<name>')
def greet(name):
    return 'hi ' + name


@app.route('/add/<a>/<b>')
def add(a, b):
    return '{}'.format(a+b)

@app.route('/real-add/<a>/<b>')
def real_add(a, b):
    return '{}'.format(int(a) + int(b))

@app.route('/converted-add/<int:a>/<int:b>')
def converted_add(a, b):
    return '{}'.format(a+b)

if __name__ == '__main__':
    app.run(debug=True)

