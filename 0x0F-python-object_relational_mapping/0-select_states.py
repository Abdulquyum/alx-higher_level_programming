#!/usr/bin/python3

import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="hbtn_0e_0_usa", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM hbtn_0e_0_usa.states ORDER BY states.id")
rows = cur.fetchall()
for row in rows:
	print(row)
conn.close()
cur.close()
