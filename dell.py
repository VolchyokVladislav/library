from db import Readers, Books, engine
from sqlalchemy.orm import sessionmaker

import MySQLdb

db = MySQLdb

db = MySQLdb.connect('127.0.0.1', 'root', 'adgjl\'', db='library')
c = db.cursor()
c.execute('select * from readers where reader_id=%s or reader_id=%s ', (1, 2))
print(c.fetchone())


#class Dell_Reader:

    #def __init__(self, reader_id):
     #   Session = sessionmaker(bind=engine)
      #  session = Session()
       # session.delete(Readers(reader_id))
        #session.commit()


#vlad = Dell_Reader('1')