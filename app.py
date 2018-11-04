import os
from flask import Flask
from flask import  Blueprint, request, jsonify
from datastore import Datastore


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
    print(ds.list_users('user'))
    return 'iam working'



if __name__ == '__main__':
    app.run()


