#!/usr/bin/python3
"""
Prints the State object with the name passed as an
argument from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = sys.argv[4]
    state = session.query(State).filter_by(name=state_name).first()
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
