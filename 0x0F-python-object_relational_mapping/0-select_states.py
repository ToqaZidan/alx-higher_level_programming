#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
from sys import argv

if __name__ == "__main__":

    """
    Connect to the database using host and port by default
    """
    db_connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        userName=argv[1],
        password=argv[2],
        database=argv[3]
    )

    """ Create a object with cursor() method """
    cur = db_connect.cursor()

    """ Execute the query """
    cur.execute("SELECT * FROM STATES")

    """ Fetch all rows in a list of lists """
    states = cur.fetchall()

    """ Print the elements """
    for state in states:
        print(state)
