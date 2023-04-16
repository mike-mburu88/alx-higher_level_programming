#!/usr/bin/python3
"""create a list of a state objects from the database
Its usage can fetch username, password and name
"""

from sqlalchemy import create_engine
import sys
import sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ = "__main__":
    emgine = create_engine("mysql+mysqldb://{}:@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3],pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(state.id):
        print("{}: {}".format(state.id, state.name))
