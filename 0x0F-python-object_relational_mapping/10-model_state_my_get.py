#!/usr/bin/python3
"""A code that prints the object with a name argument passed from a database
should take 3 arguments
username
password
database name
and connnects to the default localhost at port(3306)
"""

from sqlaclhemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    Session = sessionmaker()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3], pool_pre_ping=True)
    session = Session(bind=engine)
    Base.metadata.createall(engine)
    instances = session.query(State).filter(State.name == argv[4].all()
    if instances:
        for instances in instance:
            if instance.name == argv[4]:
                print("{}".format(instance.id))
    else:
        print("Not found")
    sessio.close()
