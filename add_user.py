from db import Readers, Books, engine
from sqlalchemy.orm import sessionmaker


class Add_Reader:

    def __init__(self):
        name = input('name: ')
        fullname = input('fullname:')
        phone = input('phone: ')
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(Readers(name=name, fullname=fullname, phone_number=phone))
        session.commit()

class Add_Book:

    def __init__(self):
        book_name = input('book name: ')
        autor = input('autor name: ')
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(Books(book_name=book_name, autor=autor))
        session.commit()


user = Add_Reader()