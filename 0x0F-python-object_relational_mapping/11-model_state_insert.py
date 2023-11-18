#!/usr/bin/python3
"""
    Adds a new State object to the database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys


def add_new_object():
    """Creates a new object and adds it to the database"""
    user, passwd, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
            f'mysql+mysqldb://{user}:'
            f'{passwd}@localhost:3306/{database}', pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("four arguments are needed")
        sys.exit(1)

    add_new_object()
