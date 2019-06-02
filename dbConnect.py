import pymysql
conn = pymysql.connect(host='localhost',user='pi', passwd='Skram1Skram1', db='irrigation')
cur = conn.cursor()
cur.execute("SELECT * FROM moisture")
