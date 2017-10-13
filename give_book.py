from db import Readers, Books, Read_Book, engine
from sqlalchemy.orm import sessionmaker


class Give_Book:

    def __init__(self):
        id = input("reader_id: ")
        book = input("book_id: ")
        Session = sessionmaker(bind=engine)
        session = Session()
        for v in session.query(Readers.reader_id):
            for u in v:
                if u == int(id):
                    for f in session.query(Books.book_id):
                        for h in f:
                            if h == int(book):
                                session.add(Read_Book(reader_id=id, book_id=book))

                                session.commit()
                            else:
                                print('no book')
                else:
                    print('you are not in the list of users')

reasdV = Give_Book()