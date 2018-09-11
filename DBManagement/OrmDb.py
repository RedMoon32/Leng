from sqlalchemy import create_engine, Integer, String, Column, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from collections import namedtuple
from sqlalchemy.orm import sessionmaker

class User:

    __tablename__= 'users'

    chat_id = Column(Integer,primary_key=True)
    name = Column(String)

    def __repr__(self):
        return '({} {})'.format(self.chat_id, self.name)

class Utils:

    def __init__(self, db_file='Ext.db'):
        self.engine = create_engine('sqlite:///{}'.format(db_file))
        self.create_tables()
        Session = sessionmaker()
        self.session = Session(autocommit=True)

    def check_code(self):
        self.tb_usesession.query(filter)


    def create_tables(self):
        base = declarative_base(bind=self.engine)
        base.metadata.create_all()


if __name__ == '__main__':
    pass
