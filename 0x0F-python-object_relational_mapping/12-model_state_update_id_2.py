#!/usr/bin/python3
"""
Script that changes the name of a State object
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
    State = Session.query(State).filter(id=2).first()
    State.name = "New Mexico"
    Session.commit()