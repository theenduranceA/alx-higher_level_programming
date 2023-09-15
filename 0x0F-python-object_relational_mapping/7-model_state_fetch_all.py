#!/usr/bin/python3
"""Script that lists all State objects from the database hbtn_0e_6_usa."""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1],
        argv[2],
        argv[3]),
        pool_pre_ping=True)

    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    for data in session.query(State).order_by(State.id).all():
        print("{}: {}".format(data.id, data.name))
