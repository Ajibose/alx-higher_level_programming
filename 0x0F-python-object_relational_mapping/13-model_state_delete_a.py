#!/usr/bin/python3
"""
    Delete all states object based on a name that contains a
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_state_a():
    """
        Deletes all object with name that contains a
    """
    user, passwd, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
            f'mysql+mysqldb://{user}:'
            f'{passwd}@localhost:3306/{database}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State).filter(State.name.like('%a%'))
    for row in rows:
        session.delete(row)

    session.commit()


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Requires three arguments")
        sys.exit(1)

    delete_state_a()
