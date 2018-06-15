#!/usr/bin/python
from flask import request, Response
from flask import Flask
import json



APP = Flask(__name__)



@APP.route('/', methods=['POST'])
def route_function():
    """
    Function to handle "/" route POST call. Can create multiple functions to handle multiple routes.
    """
    body = request.json
    return Response(json.dumps(body), status=200, mimetype='application/json')

    


if __name__ == '__main__':
    APP.run(host="0.0.0.0", port=8080, threaded=True)
#gunicorn  -w 10 --threads 12 sampleFlaskApp:APP
