from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
class DAO():
    def __init__(self):
        self.session = None
        try:
            engine = create_engine('sqlite:///db.db', echo=False)
            Session = sessionmaker(bind=engine)
            self.session = Session()
        except Exception as err:
            raise Exception(err.message)
