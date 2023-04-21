#!/usr/bin/python3
"""a codebase that lists all City objects according to respective State
Takes three arguments
    username
    password
    database name
Connects to default localhost and default port (3306)
"""

from sqlalchemy import create_engine
from sys import argv
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from sqlalchemy.orm import relationship
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    session = Session(bind=engine)
    for city, state in session.query(City, State).filter(
            State.id == City.state_id).order_by(City.id).all():
        print("{:d}: {} -> {}".format(city.id, city.name, state.name))
    session.close()
