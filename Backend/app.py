import datetime

from datasupport import *
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Database Stuff
con = sqlite3.connect("./database.db")

rows = get_rows(con)
columns = get_columns(con)

con.commit()
con.close()
# End database stuff


class Data(Resource):
    def get(self):
        data = {
            # 'data-rows': rows,
            'data-columns': columns
        }

        return data


api.add_resource(Data, '/')


if __name__ == '__main__':
    app.run()
