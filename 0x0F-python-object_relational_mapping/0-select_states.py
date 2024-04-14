#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM hbtn_0e_0_usa.states ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
	    print(row)
