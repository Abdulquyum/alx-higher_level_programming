#!/usr/bin/python3
""" Lists all cities in the hbtn_0e_4_usa
    database
"""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM cities ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()
    cur.close()
