import pymysql

con = pymysql.connect("localhost", "root", "root", "quotes")
cur = con.cursor()

sql = "SELECT qSpeaker, qTxt FROM quotes ORDER BY RAND() LIMIT 1"

cur.execute(sql)
res = cur.fetchone()

print("{} said : {}".format(res[0], res[1]))