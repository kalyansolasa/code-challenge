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
    ds = Datastore()
    res = []
    users = ds.list_users('test')
    for user in users:
        res.append(dict(user))
    return Response(json.dumps(res),  mimetype='application/json')



if __name__ == '__main__':
    app.run()


