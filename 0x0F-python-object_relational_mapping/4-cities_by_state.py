#!/usr/bin/python3
"""
    lists all states from the database hbtn_0e_0_usa using MySQLdb
"""
import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(
            host='localhost', user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = conn.cursor()

    cur.execute("SELECT * FROM cities JOIN states ORDER BY id")

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()
