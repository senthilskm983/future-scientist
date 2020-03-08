"""
    Sample Web server application using Flask
"""

from flask import Flask, request, render_template
APP = Flask(__name__, template_folder='template/')

VALID_PASSWORD = 'test'


@APP.route('/', methods=('GET',))
def home():
    return render_template('sample_login.html')


@APP.route('/action_page', methods=('POST',))
def action():
    name = request.form.get('uname')
    password = request.form.get('psw')
    if password == VALID_PASSWORD:
        return 'Welcome %s ' % name
    return 'Password invalid'


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=80, debug=True)