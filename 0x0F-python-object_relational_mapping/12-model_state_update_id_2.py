#!/usr/bin/python3
"""Update the name of a state object"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


def update_state_by_id():
    """Update a state object"""
    user, passwd, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
            f'mysql+mysqldb://{user}:'
            f'{passwd}@localhost:3306/{database}', pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    obj = session.query(State).filter(State.id == 2).one_or_none()
    if obj is not None:
        obj.name = "New Mexico"
    else:
        print("obj not found")

    session.commit()


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Requires three argument")
        sys.exit(1)

    update_state_by_id()
