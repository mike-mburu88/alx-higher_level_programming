#!/usr/bin/python3
"""A script that outputs all city objects
takes the arguments:
username
password
database name
Connects to a localhost default port 3306
"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import aliased
from model_state import State, Base
from model_city import City
from sys import argv

if __name__ == "__main__":
    Session = sessionmaker()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    result = (session.query(State.name, City.id, City.name).filter(
        State.id == City.state_id).order_by(City.id).all())
    for i in result:
        print("{}: ({:d}) {}".format(i[0], i[1], i[2]))
    session.close()
