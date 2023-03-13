from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

engine = create_engine('postgresql://adv:mypass1!@127.0.0.1:5433/adv_db')
Session_maker = sessionmaker(bind=engine)
session_q = Session(bind=engine)