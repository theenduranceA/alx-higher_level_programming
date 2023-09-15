#!/usr/bin/python3
"""Script that creates the State “California” with the
City “San Francisco” from the database hbtn_0e_100_usa."""

from sys import argv
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1],
        argv[2],
        argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)
    session.add(new_city)
    session.commit()
