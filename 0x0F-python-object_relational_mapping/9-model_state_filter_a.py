#!/usr/bin/python3
"""List all the state object that contain `a` letter from the database."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in (
        session.query(State)
        .filter(State.name.ilike("%a%"))
        .order_by(State.id)
        .all()
    ):
        print(f"{state.id}: {state.name}")

    session.close()
