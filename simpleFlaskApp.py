#!/usr/bin/python
from flask import request, Response
from flask import Flask
import json
import bjoern
import uuid
import sqlite3

import math
APP = Flask(__name__)


import time
@APP.route('/', methods=['POST'])
def route_function_POST():
    """
    Function to handle "/" route POST call. Can create multiple functions to handle multiple routes.
    """
    body = request.json
    return Response(json.dumps(body), status=200, mimetype='application/json')

    
@APP.route('/', methods=['GET'])
def route_function_GET():
    """
    Function to handle "/" route GET call. Can create multiple functions to handle multiple routes.  """
    conn = sqlite3.connect('k.db')
    conn.close()
    return Response("done", status=200, mimetype='application/json')

if __name__ == '__main__':
    print("running bjoern")
    bjoern.run(APP, '0.0.0.0', 8080, reuse_port=True)

    #gunicorn  -w 10 --threads 12 sampleFlaskApp:APP
