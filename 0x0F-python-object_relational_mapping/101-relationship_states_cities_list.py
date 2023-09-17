#!/usr/bin/python3
"""Script that lists all State objects, and corresponding
City objects, contained in the database hbtn_0e_14_usa."""

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

    for data in session.query(State).order_by(State.id):
        print("{}: {}".format(data.id, data.name))
        for city in data.cities:
            print("    {}: {}".format(city.id, city.name))
