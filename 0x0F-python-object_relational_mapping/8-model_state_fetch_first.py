#!/usr/bin/python3
"""A code that prints the first 'State' object from database
takes the three arguments
username
password
name
Connects to the default localhost and default port (3306)
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    Session = sessionmaker()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    instance = session.query(State).first()
    if instance:
        print("{}: {}".format(instance.id, instance.name))
    else:
        print("Nothing")
    session.close()
