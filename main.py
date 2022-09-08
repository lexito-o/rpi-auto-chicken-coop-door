#!/usr/bin/python3

from dotenv import dotenv_values
from flask import Flask
import utils.gpio as utils

app = Flask(__name__)
config = dotenv_values(".env")

@app.route('/')
def index():
    return str(utils.toggle_door())

def setup():
    utils.setup(config)

if __name__ == '__main__':
    setup()
    app.run(debug=True, host=config['HOST'], port=config['PORT'])
