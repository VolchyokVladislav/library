from db import Readers, Books, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

class Add_Reader:
    def __init__(self, name, fullname, phone_number):
        session.add(Readers(name=name, fullname=fullname, phone_number=phone_number))
        session.commit()

class Add_Book:
    def __init__(self, book_name, autor):
        session.add(Books(book_name=book_name, autor=autor))
        session.commit()

Vika = Add_Reader('Vica', 'Volchyok', '+375253366885')