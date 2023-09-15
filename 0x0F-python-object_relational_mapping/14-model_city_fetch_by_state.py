#!/usr/bin/python3
"""Script  that prints all City objects from the database hbtn_0e_14_usa."""

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

    for data in session.query(City).join(State).order_by(asc(City.id)).all():
        print("{}: ({}) {}".format(data.state.name, data.id, data.name))
    session.commit()
