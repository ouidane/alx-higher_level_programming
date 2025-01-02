#!/usr/bin/python3
"""Delete all state objects with the name containing the letter `a`."""
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

    session.query(State).filter(State.name.ilike("%a%")).delete(
        synchronize_session="fetch"
    )
    session.commit()

    session.close()
