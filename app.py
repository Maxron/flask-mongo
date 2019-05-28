import os
from flask import Flask, request
from pymongo import MongoClient

client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'],27017)
# client = MongoClient('mongodb://127.0.0.1',27017)
db = client.test

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!<h1>'

@app.route('/data', methods=['POST'])
def add_data():
    if request.method == 'POST':
        print('json: ', request.json)
        db.data.insert_one(request.json)
    return 'ok'
