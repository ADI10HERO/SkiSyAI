from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///skiai.db', echo=True)
Base = declarative_base()

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    district = Column(String)

    def __init__(self, username, password, district):
        self.username = username
        self.password = password
        self.district = district

class Data(Base):

    __tablename__ = "data"

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    gender = Column(String)
    age = Column(String)
    Historyofpresentillness = Column(String(200))
    history1 = Column(String)
    history2 = Column(String)
    history3 = Column(String)
    history4 = Column(String)
    symptom1 = Column(String)
    symptom2 = Column(String)
    symptom3 = Column(String)
    symptom4 = Column(String)
    symptom5 = Column(String)
    Drugshistory = Column(String(200))
    path = Column(String(100))
    prediction = Column(String)

    def __init__(self,firstname,lastname,gender,age,Historyofpresentillness,
                history1,history2,history3,history4,
                symptom1,symptom2,symptom3,symptom4,symptom5,
                Drugshistory,path,prediction):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age
        self.Historyofpresentillness = Historyofpresentillness
        self.history1 = history1
        self.history2 = history2
        self.history3 = history3
        self.history4 = history4
        self.symptom1 = symptom1
        self.symptom2 = symptom2
        self.symptom3 = symptom3
        self.symptom4 = symptom4
        self.symptom5 = symptom5
        self.Drugshistory = Drugshistory
        self.path = path
        self.prediction = prediction
# create tables

Base.metadata.create_all(engine)
Base.metadata.create_all(engine)