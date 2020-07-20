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
    isDoctor = Column(String)
    city = Column(String)

    def __init__(self, username, password, isDoctor, city):
        self.username = username
        self.password = password
        self.isDoctor = isDoctor
        self.city = city


class Data(Base):

    __tablename__ = "data"

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    gender = Column(String)
    age = Column(String)
    country = Column(String)
    state = Column(String)
    city = Column(String)
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
    user_name = Column(String)
    comment = Column(String(450))
    status = Column(Integer)
    def __init__(self,firstname,lastname,gender,age,country,state,city,Historyofpresentillness,
                history1,history2,history3,history4,
                symptom1,symptom2,symptom3,symptom4,symptom5,
                Drugshistory,path,prediction,user_name,comment,status):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age
        self.country = country
        self.state = state
        self.city = city
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
        self.user_name = user_name
        self.comment = comment
        self.status = status
# create tables 
class Frequency(Base):

    __tablename__ = "frequency"

    id = Column(Integer, primary_key=True)
    city = Column(String)
    disease = Column(String)
    freq = Column(Integer)
    def __init__(self, city, disease,freq):
        self.city = city
        self.disease = disease
        self.freq = freq

Base.metadata.create_all(engine)
Base.metadata.create_all(engine)