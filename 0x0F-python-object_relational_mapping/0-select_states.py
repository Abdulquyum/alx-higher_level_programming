#!/usr/bin/python3

import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(user="root", passwd="root", db="hbtn_0e_0_usa")
    cur = conn.cursor()
    cur.execute("SELECT * FROM hbtn_0e_0_usa.states ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
	    print(row)
    conn.close()
    cur.close()
