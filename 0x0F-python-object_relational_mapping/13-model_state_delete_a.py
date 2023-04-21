#!/usr/bin/python3
"""A codebbase that deletes State objects with
 a name that contains a as a letter
the code takes all arguments:
password
username
database name
Connects using a default localhost and default port 3306
"""

from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker()
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    instances = session.query(State).filter(State.name.like('%a')).all()
    if instances:
        for instance in instances:
            session.delete(instance)
        session.commit()
    session.close()
