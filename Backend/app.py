import datetime

from datasupport import *
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

data = {
    'timestamp': str(datetime.datetime.now().year),
    'other': 'foo'
}


class Data(Resource):
    def get(self):
        db_testing()
        return data


api.add_resource(Data, '/')


if __name__ == '__main__':
    app.run()
