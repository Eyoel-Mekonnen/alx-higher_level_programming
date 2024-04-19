#!/usr/bin/python3
"""prints all city objects from database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import joinedload

if __name__ == "__main__":
    if (len(sys.argv) != 4):
        print("Number of argument not equal")

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).options(joinedload(City.state)).all()
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))
