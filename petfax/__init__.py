from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'My first Flask App!'


app.route('/pets')
def pets():
    return 'This is the PETS page!'

