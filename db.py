from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Readers(Base):
    __tablename__ = 'readers'

    reader_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    fullname = Column(String(20))
    phone_number = Column(String(15))

class Books(Base):
    __tablename__ = 'books'

    book_id = Column(Integer, primary_key=True, autoincrement=True)
    book_name = Column(String(20))
    autor = Column(String(20))

engine = create_engine('mysql+mysqldb://root:adgjl\'@localhost:3306/library', echo=True)
Base.metadata.create_all(engine)

