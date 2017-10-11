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

#Session = sessionmaker(bind=engine)
#session = Session()
#user = Readers(name='Vika', fullname='Vol', phone_number='1111')
#session.add(user)
#user.phone_number = '222222'
#session.commit()
#print(user.reader_id)
#our_user = session.query(Readers).filter_by(name='Vlad').first()
#print(dict(our_user))
#book = Add_Book()