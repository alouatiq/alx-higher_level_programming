#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    results = (session.query(City, State)
               .filter(City.state_id == State.id)
               .order_by(City.id).all())

    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
