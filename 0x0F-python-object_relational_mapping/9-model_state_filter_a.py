#!/usr/bin/python3
"""List all containing letter a."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if (len(sys.argv) != 4):
        print("Number of Argument not correct")
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    value = session.query(State).filter(State.name.like('%a%')).all()
    for instance in value:
        print("{}: {}".format(instance.id, instance.name))
