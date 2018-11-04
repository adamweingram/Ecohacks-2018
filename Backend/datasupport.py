import datetime, csv, sqlite3


def get_rows(con):
    """
    Query the database and return the values as a list
    :param con: the connection object
    :return: database values in an array
    """
    cur = con.cursor()
    cur.execute("SELECT * FROM given_data")

    rows = cur.fetchall()

    return rows


def db_testing():
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    cur.execute("CREATE TABLE given_data (reading_time text, chw_total text, hw_total text, hw_kl text, chw_kl text, hw_cob text, chw_cob text, hw_SE1 text, chw_SE1 text, hw_SE2 text, chw_SE2 text, hw_SSB text, chw_SSB text, hw_SSM text, chw_SSM text, hw_SAAC text, chw_SAAC text, total_sunpower_kwh text);")

    insert_vars = [str(datetime.datetime.now()), "171.3230092", "201.4196262", "21.8",	"42.4",	"9.3", "14.7", "147.5", "82.4",	"0", "9.00225", "13.76", "NULL", "NULL", "NULL", "NULL", "NULL", "4863.202475"]

    cur.execute("INSERT INTO given_data (reading_time, chw_total, hw_total, hw_kl, chw_kl, hw_cob, chw_cob, hw_SE1, chw_SE1, hw_SE2, chw_SE2, hw_SSB, chw_SSB, hw_SSM, chw_SSM, hw_SAAC, chw_SAAC, total_sunpower_kwh) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", insert_vars)

    print(get_rows(con))

    con.commit()
    con.close()

