import os
from flask import Flask
from flask import  Blueprint, request, jsonify, Response
from datastore import Datastore
import json


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def hello():
    return "Hello World!"


'''@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)'''

@app.route('/listusers')
def list_users():
    filters = []
    territory = request.args.get('territory', default = '', type = str)
    los = request.args.get('line_of_service', default = '', type = str)
    last_name = request.args.get('last_name', default = '', type = str)
    if territory:
        filters.append(('territory','=', territory))
    if los :
        filters.append(('line_of_service','=', los))
    if last_name:
        filters.append(('last_name','=', last_name))

    ds = Datastore()
    res = []
    users = ds.list_users('test', filters)
    for user in users:
        res.append(dict(user))
    return Response(json.dumps(res),  mimetype='application/json')



if __name__ == '__main__':
    app.run()


