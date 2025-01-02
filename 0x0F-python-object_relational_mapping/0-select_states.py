#!/usr/bin/python3
"""Connect & List all states from the database hbtn_0e_0_usa."""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `states`")
    [print(state) for state in cursor.fetchall()]

    cursor.close()
    conn.close()
