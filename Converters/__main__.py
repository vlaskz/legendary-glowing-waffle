from flask import Flask, jsonify, request, g
from werkzeug.routing import BaseConverter, ValidationError

_USERS = {'1':'Tarek', '2':'Freya', '3':'Tyr', '4':'Odin'}
_IDS = {val: id for id, val in _USERS.items()}

app = Flask(__name__)

class RegisteredUser(BaseConverter):
    def to_python(self, value):
        if value in _USERS:
            return _USERS[value]
        raise ValidationError()
    
    def to_url(self, value):
        return _IDS[value]

@app.before_request
def authenticate():
    if request.authorization:
        g.user = request.authorization['username']
    else:
        g.user = 'Anonymous'

app.url_map.converters['registered'] = RegisteredUser

@app.route('/api/v1/person/<registered:name>')
def get_person(name):
    response = jsonify({
           
            'logged_user':g.user,
            'name':name
        })
    return response

if(__name__) == '__main__':
    app.run()