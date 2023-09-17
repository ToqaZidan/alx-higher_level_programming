#!/usr/bin/python3
"""Script that lists all State objects from the database hbtn_0e_6_usa"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == '__main__':

    """Make engine for database"""
    db_link = "mysql+mysqldb://{}:{}@localhost/{}"\
        .format(argv[1], argv[2], argv[3])

    """ Make session"""
    engine = create_engine(db_link)
    Session = sessionmaker(bind=engine)

    Session = Session()

    """ Query to database """

    state = Session.query(State).order_by(State.id).first()
    if state is not None:    
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
