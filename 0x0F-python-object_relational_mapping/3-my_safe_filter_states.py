#!/usr/bin/python3
"""Prevent SQL Injection."""
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
    )

    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM `states` WHERE BINARY `name` = %s", (sys.argv[4],)
    )
    [print(state) for state in cursor.fetchall()]

    cursor.close()
    conn.close()
