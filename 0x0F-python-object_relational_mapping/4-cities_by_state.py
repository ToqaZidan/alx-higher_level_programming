#!/usr/bin/python3
""" Script that lists all cities from the database hbtn_0e_4_usa
"""


import MySQLdb as db
from sys import argv

""" Script that lists all cities from the database hbtn_0e_4_usa """
if __name__ == '__main__':

    """
    Connect to the database using host and port by default
    """
    db_connect = db.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        )

    """ Create a object with cursor() method """
    cur = db_connect.cursor()

    """ Execute the query """
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
               JOIN states ON cities.state_id = states.id \
               ORDER BY cities.id ASC")

    """ Fetch all rows in a list of lists """
    rowcount = cur.fetchall()

    """ Print the elements """
    if rowcount != 0:
        for row in rowcount:
            print(row)
