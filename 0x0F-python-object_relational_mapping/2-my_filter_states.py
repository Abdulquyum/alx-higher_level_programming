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
    cur.execute("SELECT * FROM states ORDER BY states.id")
    [print(state) for state in cur.fetchall() if state[1] == sys.argv[4]]
