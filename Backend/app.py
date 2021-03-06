import datetime

from datasupport import *
from flask import Flask
from flask import jsonify
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

@app.route('/ohno.js')
def summary():
    data = "{'columns': " + str(columns) + "}"

    ret = 'var foo = {}'.format(data)
    print(ret)
    return ret


if __name__ == '__main__':
    app.run()
