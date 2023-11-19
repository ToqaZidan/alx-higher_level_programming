#!/usr/bin/python3
"""Script that lists all State objects from the database hbtn_0e_6_usa"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City, Base

if __name__ == '__main__':

    """Make engine for database"""
    db_link = "mysql+mysqldb://{}:{}@localhost/{}"\
        .format(argv[1], argv[2], argv[3])

    """ Make session"""
    engine = create_engine(db_link)
    Session = sessionmaker(bind=engine)

    Session = Session()

    """ Query to database """

    for city, state in Session.query(City, State)\
        .filter(City.state_id == State.id).order_by(City.id):

        print("{}: ({}) {}".format(state.name, city.id, city.name))

