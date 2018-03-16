from flask import Flask, render_template, make_response, request, Response 

app = Flask(__name__)

# Modification 2: Define your own Flask app routes and functions
@app.route('/')
def index():
    return ("mew")


def getAPP():
    return app