import csv, sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE t (time, chw_total, hw_total, hw_kl, chw_kl, hw_cob, chw_cob,hw_SE1,chw_SE1,hw_SE2,chw_SE2,hw_SSB,chw_SSB,hw_SSM,chw_SSM,hw_SAAC,chw_SAAC,total_sunpower_kwh);") # use your column names here

with open('DataForTesting.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['time'], i['chw_total'],i['hw_total'], i['hw_kl'],i['chw_kl'], i['hw_cob'], i['chw_cob'], i['hw_SE1'],i['chw_SE1'], i['hw_SE2'],i['chw_SE2'], i['hw_SSB'], i['chw_SSB'], i['hw_SSM'], i['chw_SSM'], i['hw_SAAC'],i['chw_SAAC'], i['total_sunpower_kwh']) for i in dr]

cur.executemany("INSERT INTO t (time, chw_total, hw_total, hw_kl, chw_kl, hw_cob, chw_cob,hw_SE1,chw_SE1,hw_SE2,chw_SE2,hw_SSB,chw_SSB,hw_SSM,chw_SSM,hw_SAAC,chw_SAAC,total_sunpower_kwh) VALUES (?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()