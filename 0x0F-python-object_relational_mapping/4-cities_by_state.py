#!/usr/bin/python3
"""List Cities by States."""
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
    )

    cursor = conn.cursor()
    cursor.execute(
        """SELECT cities.id, cities.name, states.name
        FROM states, cities
        WHERE cities.state_id = states.id
        ORDER BY cities.id"""
    )
    [print(state) for state in cursor.fetchall()]

    cursor.close()
    conn.close()
