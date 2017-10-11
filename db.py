from sqlalchemy import Column, Integer, String, create_engine, TIMESTAMP, ForeignKey, BOOLEAN
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Readers(Base):
    __tablename__ = 'readers'

    reader_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    fullname = Column(String(20))
    phone_number = Column(String(15))
    read_now = Column(BOOLEAN, default=False)
    children = relationship('Read_Book', remote_side='Read_Book.reader_id')

class Books(Base):
    __tablename__ = 'books'

    book_id = Column(Integer, primary_key=True, autoincrement=True)
    book_name = Column(String(20))
    autor = Column(String(20))
    in_library = Column(BOOLEAN, default=True)
    ch1 = relationship('Read_Book', remote_side='Read_Book.book_id')

class Read_Book(Base):
    __tablename__ = 'read_book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    reader_id = Column(Integer, ForeignKey('readers.reader_id'))
    book_id = Column(Integer, ForeignKey('books.book_id'))
    timestamp = Column(TIMESTAMP, default=0)

class Stop_list(Base):
    __tablename__ = 'stop_list'

    reader_id = Column(Integer, primary_key=True, autoincrement=True)
    minus = Column(Integer)


engine = create_engine('mysql+mysqldb://root:adgjl\'@localhost:3306/library', echo=True)
Base.metadata.create_all(engine)

