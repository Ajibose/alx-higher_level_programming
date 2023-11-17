#!/usr/bin/python3
"""
    lists all cities of a state from the database hbtn_0e_0_usa using MySQLdb
"""
import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(
            host='localhost', user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = conn.cursor()

    cur.execute(
            "SELECT c.name FROM cities c\
            WHERE c.state_id=(\
            SELECT s.id FROM states s WHERE s.name=%s)",
            (sys.argv[4],))

    rows = cur.fetchall()
    tuple_rows = tuple(row[0] for row in rows)
    print(*tuple_rows, sep=', ')
    cur.close()
    conn.close()
