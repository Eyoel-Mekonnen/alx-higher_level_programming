#!/usr/bin/python3
"""Change the state object from database."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if (len(sys.argv) != 4):
        print("Number of argument not correct")
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    value = session.query(State).filter(State.id == 2).first()
    if (value):
        value.name = 'New Mexico'
    session.commit()
