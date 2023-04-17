#!/usr/bin/python3
"""A python codebase that add an object Louisiana to a database
takes 3 arguments:
username
password
name of the database
Connects to a default localhost at port 3306
"""

from model_state import State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    Session = Sessionmaker()
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True)
    session = Sessionmaker(bind=engine)
    Base.metadata.createall(engine)
    state = State(name="Louisiana")
    session.add(state)
    session.commit()
    print(state.id)
    session.close()
   
