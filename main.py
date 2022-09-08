#!/usr/bin/python3

from dotenv import dotenv_values
from flask import Flask

app = Flask(__name__)
config = dotenv_values(".env")

@app.route('/')
def index():
    return 'aaa'

if __name__ == '__main__':
    app.run(debug=True, host=config['HOST'], port=config['PORT'])
