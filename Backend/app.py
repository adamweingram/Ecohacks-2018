import datetime

from datasupport import *
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Data(Resource):
    def get(self):
        con = sqlite3.connect(":memory:")
        cur = con.cursor()
        cur.execute(
            "CREATE TABLE given_data (reading_time text, chw_total text, hw_total text, hw_kl text, chw_kl text, hw_cob text, chw_cob text, hw_SE1 text, chw_SE1 text, hw_SE2 text, chw_SE2 text, hw_SSB text, chw_SSB text, hw_SSM text, chw_SSM text, hw_SAAC text, chw_SAAC text, total_sunpower_kwh text);")

        insert_vars = [str(datetime.datetime.now()), "171.3230092", "201.4196262", "21.8", "42.4", "9.3", "14.7",
                       "147.5", "82.4", "0", "9.00225", "13.76", "NULL", "NULL", "NULL", "NULL", "NULL", "4863.202475"]

        cur.execute(
            "INSERT INTO given_data (reading_time, chw_total, hw_total, hw_kl, chw_kl, hw_cob, chw_cob, hw_SE1, chw_SE1, hw_SE2, chw_SE2, hw_SSB, chw_SSB, hw_SSM, chw_SSM, hw_SAAC, chw_SAAC, total_sunpower_kwh) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
            insert_vars)

        cur.execute(
            "INSERT INTO given_data (reading_time, chw_total, hw_total, hw_kl, chw_kl, hw_cob, chw_cob, hw_SE1, chw_SE1, hw_SE2, chw_SE2, hw_SSB, chw_SSB, hw_SSM, chw_SSM, hw_SAAC, chw_SAAC, total_sunpower_kwh) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
            insert_vars)

        values = get_rows(con)

        con.commit()
        con.close()

        data = {
            'timestamp': str(datetime.datetime.now()),
            'other': 'foo',
            'testing': values
        }

        return data


api.add_resource(Data, '/')


if __name__ == '__main__':
    app.run()
