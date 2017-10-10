from db import Readers, Books, engine
from sqlalchemy.orm import sessionmaker


class Give_Book:
    Session = sessionmaker(bind=engine)
    session = Session()