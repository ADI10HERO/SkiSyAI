import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import *

engine = create_engine('sqlite:///skiai.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
s = Session()

'''
# Data ka format
Data(fname,lname,gender,age,Historyofpresentillness,
                    history1,history2,history3,history4,
                    symptom1,symptom2,symptom3,symptom4,symptom5,
                    Drugshistory,destination,model_pred,user_name,comment=None,status='0')
'''
res = s.query(Frequency).all()
print(res) 
for r in res:
    print(r.city,r.freq,r.disease)
