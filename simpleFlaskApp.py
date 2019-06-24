#!/usr/bin/python
from flask import request, Response
from flask import Flask
import json
import bjoern
import uuid
import sqlite3

import math
app = Flask(__name__)
import requests

import time
@app.route('/', methods=['POST'])
def route_function_POST():
    """
    Function to handle "/" route POST call. Can create multiple functions to handle multiple routes.
    """
    body = request.json
    return Response(json.dumps(body), status=200, mimetype='application/json')

    
@app.route('/', methods=['GET'])
def route_function_GET():
    """
    print("in")
    Function to handle "/" route GET call. Can create multiple functions to handle multiple routes.  """
    # print("in")
    r = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    # print(r)
    return Response("done", status=200, mimetype='application/json')

if __name__ == '__main__':
    print("running bjoern")
    app.run(port=8383)
    # bjoern.run(app, '0.0.0.0', 8383, reuse_port=True)

    #gunicorn  -w 10 --threads 12 sampleFlaskApp:APP
