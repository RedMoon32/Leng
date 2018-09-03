import sys

print(sys.path)
sys.path.append('../')

from flask import Flask, request, make_response
from flask_restful import Api
from flask_restful import Resource
import sqlite3
from flask import jsonify
from functools import wraps
from DBManagement.DataBase import Manager

app = Flask(__name__)
api = Api(app)
m = Manager()


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


@app.route('/', methods=['GET', 'OPTIONS'])
def home():
    resp = 'Main page is working'
    return make_response(resp)


class set_code(Resource):
    def get(self, code):
        if m.check_temp(code):
            m.verify(code)
            return make_response(jsonify({'result': 'OK'}))
        else:
            return make_response(jsonify({'result': 'Error'}))


class test_server(Resource):
    def get(self):
        return make_response(jsonify({'result': 'Ok, server is working'}))


class add_word(Resource):
    def get(self, code, word):
        if m.check_code(code):
            m.add_word(code, word)
            return make_response(jsonify({'result': 'OK'}))
        else:
            return make_response(jsonify({'result': 'Error'}))


def init_api():
    api.add_resource(test_server, '/test_server/')
    api.add_resource(set_code, '/set_code/<code>')
    api.add_resource(add_word, '/add_word/<code>/<word>')


if __name__ == '__main__':
    init_api()
    app.run(port='5002')
