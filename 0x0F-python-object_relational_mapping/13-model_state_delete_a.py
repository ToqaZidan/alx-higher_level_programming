#!/usr/bin/python3
"""
Script that Delete a State objects
    in the database hbtn_0e_6_usa
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
    state_del = Session.query(State).filter(State.name.like('%a%')).all()
    if state_del:
        for state in state_del:
            Session.delete(state)
    Session.commit()
