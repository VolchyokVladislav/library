from db import Readers, Books, Read_Book, engine
from sqlalchemy.orm import sessionmaker


class Give_Book:

    def _init__(self):
        id = input('reader_id: ')
        book = input('book_id: ')
        Session = sessionmaker(bind=engine)
        session = Session()
        if id in session.query(Readers.reader_id) and book in session.query(Books.book_id):
            session.add(Read_Book(reader_id=id, book_id=book))
            session.commit()
        else:
            print('you are not in the list of users')

read = Give_Book()