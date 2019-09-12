import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import *

engine = create_engine('sqlite:///skiai.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User("admin","password","Yes")
session.add(user)

user = User("adi","adi","No")
session.add(user)

user = User("sam","mw","No")
session.add(user)

user = User("dinesh","iamdoc","Yes")
session.add(user)
# commit the record the database
session.commit()

session.commit()