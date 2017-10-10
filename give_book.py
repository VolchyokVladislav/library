from db import Readers, Books, Read_Book, engine
from sqlalchemy.orm import sessionmaker


class Give_Book:

    def _init__(self):
        id = input('reader_id: ')
        book = input('book_id: ')
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(Read_Book(reader_id=id, book_id=book))
        session.commit()


read = Give_Book()