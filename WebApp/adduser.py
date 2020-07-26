import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import *

engine = create_engine('sqlite:///skiai.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User("admin","password","Yes", "Mumbai")
session.add(user)

user = User("adi","adi","No", "Pune")
session.add(user)

user = User("sam","mw","No", "Delhi")
session.add(user)

user = User("prtk","kuchbhi","No", "Panaji")
session.add(user)

user = User("shaitan","shintan","Yes", "Nagpur")
session.add(user)

user = User("rj","8228","Yes", "Pune")
session.add(user)


# commit the record the database
session.commit()

session.commit()
