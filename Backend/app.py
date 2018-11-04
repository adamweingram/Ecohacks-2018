import datetime

from datasupport import *
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Data(Resource):
    def get(self):
        con = sqlite3.connect("./database.db")
        # cur = con.cursor()

        values = get_rows(con)

        con.commit()
        con.close()

        data = {
            'data-rows': values[0:20]
        }

        return data


api.add_resource(Data, '/')


if __name__ == '__main__':
    app.run()
