#!/usr/bin/python3
"""A codebase that changes the State object with an id = 2 to New Mexico in the database
the function takes the following metadata as arguments:
username
database name
password
"""

from sqlalchmey.orm import sessionmaker
from sqlaclhemy import create_engine
import sys
from model_state import State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3], pool_pre_ping=True)
    Session = sessionmaker()
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()
    session.close()
