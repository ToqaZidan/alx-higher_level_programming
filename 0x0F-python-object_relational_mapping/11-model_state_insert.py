#!/usr/bin/python3
"""
Script that add new new Satet object
    to the database hbtn_0e_6_usa
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

    """ Add new state """

    new_state = State(name= "Louisiana")
    Session.add(new_state)
    Session.commit()
    
    Session.close()
    
    """ Query to database """
    print("{}".format(new_state.id))