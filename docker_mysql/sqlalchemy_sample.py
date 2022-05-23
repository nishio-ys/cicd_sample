#!/usr/bin/env python3
"""
DB access sample program


pip install sqlalchemy mysql
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


# MySQL setting
USERNAME = 'user'
PASSWORD = 'password'
HOST = '127.0.0.1'
PORT = 3314

# MySQL, SQLite3 setting
DATABASE = 'fap_db'


Base = declarative_base()


class Fruit(Base):

    id = Column(Integer, primary_key=True)
    name = Column(String(length=255))
    __tablename__ = 'fruits'


def main(engine):
    print(engine)
    meta = Base.metadata
    meta.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(Fruit(name="Apple"))
    session.add(Fruit(name="Banana"))
    session.add(Fruit(name="Peach"))
    session.add(Fruit(name="Orange"))
    session.commit()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python %s "mysql"|"sqlite3"' % (sys.argv[0]))
        exit()

    engine = None
    if sys.argv[1] == 'mysql':
        print('MySQL')
        engine = create_engine(f'mysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/'
                               f'{DATABASE}')
    else:
        print('Sqlite3')
        engine = create_engine('sqlite:///sample_db.sqlite3',
                               echo=True)

    main(engine)
