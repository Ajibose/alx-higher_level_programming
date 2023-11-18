#!/usr/bin/python3
"""
    List all state objects that contain letter a
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State


def fetch_state_a():
    """Fetches all State objects whose name contains a"""
    user, passwd, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(user, passwd, database))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for row in rows:
        print(row.id, row.name, sep=': ')

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: filename mysql username, mysql password and database name")
        sys.exit(1)

    fetch_state_a()
