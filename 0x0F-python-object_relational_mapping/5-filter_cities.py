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
        """SELECT cities.name
        FROM states, cities
        WHERE cities.state_id = states.id
            AND states.name = %s
        ORDER BY cities.id""",
        (sys.argv[4],),
    )
    print(", ".join([state[0] for state in cursor.fetchall()]))

    cursor.close()
    conn.close()
