#!/usr/bin/python3
"""
    Defines a function that rints all city objects
"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def fetch_by_state():
    """Fetch all cities object including their state name"""
    user, passwd, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
            f'mysql+mysqldb://{user}:'
            f'{passwd}@localhost:3306/{database}', pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State.name, City.id, City.name)\
        .filter(City.state_id == State.id)
    for row in rows:
        print("{}: ({}) {}".format(row[0], row[1], row[2]))


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Requires 3 arguments")
        sys.exit(1)

    fetch_by_state()
