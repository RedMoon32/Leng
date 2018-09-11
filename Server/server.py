import sys

print(sys.path)
sys.path.append('../')

from flask import Flask, make_response
from flask_restful import Api
from flask_restful import Resource
from flask import jsonify
from DBManagement.DataBase import Manager

# from DBManagement.OrmDb import Utils

app = Flask(__name__)
api = Api(app)

# login_manager=LoginManager()
# login_manager.init_app(app);

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
    return resp


class set_code(Resource):
    def get(self, code):
        if m.check_temp(code):
            m.verify(code)
            return jsonify({'result': 'OK'})
        else:
            return jsonify({'result': 'Error'})


class test_server(Resource):
    def get(self):
        return jsonify({'result': 'OK'})


class add_word(Resource):
    def get(self, code, word):
        if m.check_code(code):
            m.add_word(code, word)
            return jsonify({'result': 'OK'})
        else:
            return jsonify({'result': 'Error'})


class login_user(Resource):
    def get(self, code):
        if m.check_code(code):
            return jsonify({'result': 'OK'})
        else:
            return jsonify({'result': 'ERROR'})


def init_api():
    api.add_resource(login_user, '/login/<code>')
    api.add_resource(test_server, '/test_server/')
    api.add_resource(set_code, '/set_code/<code>')
    api.add_resource(add_word, '/add_word/<code>/<word>')


if __name__ == '__main__':
    init_api()
    app.run(port='5000')
