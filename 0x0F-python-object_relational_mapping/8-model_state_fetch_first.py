#!/usr/bin/python3
"""this script prints the first State object from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    with Session() as session:
        f_state = session.query(State).order_by(State.id).first()

        if f_state is not None:
            print("{}: {}".format(f_state.id, f_state.name))
        else:
            print("nothing")
