#!/usr/bin/python3
"""
    displays all values in the states table of hbtn_0e_0_usa
    where name matches the argument
"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name={} ORDER BY states.id"\
            .format(sys.argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
