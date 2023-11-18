#!/usr/bin/python3
"""
    fetch the id of a state object whose name is the
    last argument passed to script
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text


def fetch_state_by_name():
    user, passwd, database, state_name = sys.argv[1], sys.argv[2],\
        sys.argv[3], sys.argv[4]

    engine = create_engine(
            f'mysql+mysqldb://{user}:'
            f'{passwd}@localhost:3306/{database}', pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State.id).filter(text("name=:name"))\
        .params(name=state_name)

    if (rows):
        for row in rows:
            print(*row)
    else:
        print("Not found")


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: filename username, mysql password,\
                    database name and state name to search")
        sys.exit(1)

    fetch_state_by_name()
