import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import *

# engine = create_engine('sqlite:///skiai.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

'''
# Data ka format
Data(fname,lname,gender,age,Historyofpresentillness,
                    history1,history2,history3,history4,
                    symptom1,symptom2,symptom3,symptom4,symptom5,
                    Drugshistory,destination,model_pred,user_name,comment=None,status='0')
'''
case=Data('tanvi','shinde','female','22','present illness','Diabetes','-','-','-','Itching','-','-','-','-','drug history','/nothing','Acne','tanvi','None',0)
session.add(case)
case=Data('sansa','stark','female','22','present illness','Diabetes','-','-','-','Itching','-','-','-','-','drug history','/nothing','Tinea','sns','None',0)
session.add(case)
case=Data('arya','stark','female','22','present illness','Diabetes','-','-','-','Itching','-','-','-','-','drug history','/nothing','Tinea','ans','None',0)
session.add(case)

session.commit()

session.commit()