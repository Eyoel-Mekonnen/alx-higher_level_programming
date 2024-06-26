#!/usr/bin/python3
"""Add a new state object called Louisiana"""
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
    new_user = State(name='Louisiana')
    session.add(new_user)
    session.commit()
    value = session.query(State).filter(State.name == 'Louisiana').first()
    print(value.id)
