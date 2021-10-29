# Test line
from waitress import serve
from wireframe import app
from dash_auth import BasicAuth

VALID_USERNAME_PWD_PAIR = open('login_creds.txt').readlines()[0].split(':')

auth = BasicAuth(app, {VALID_USERNAME_PWD_PAIR[0]: VALID_USERNAME_PWD_PAIR[1]})
app.config['suppress_callback_exceptions']=True

serve(app.server, port=3000)
