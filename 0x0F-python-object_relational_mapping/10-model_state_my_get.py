#!/usr/bin/python3
"""
Script that lists all State objects contatin letter 'a'
    from the database hbtn_0e_6_usa
"""


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

    state_name = argv[4]
    states = Session.query(State).filter(State.name == state_name).first()
    for state in states:
        print("{}".format(state.id))
    if state is None:
        print("Not found")
