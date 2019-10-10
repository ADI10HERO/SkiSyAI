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
# query = s.query(Frequency)
# res = query.all()
# print(query) 
# for r in res:
#     print(r.city,r.disease,r.freq)
#     # print(r.id,r.city,r.prediction,r.status,r.comment)
row2 = Frequency("Mumbai","Acne",43)
s.add(row2)
row2 = Frequency("Pune","Acne",53)
s.add(row2)
row2 = Frequency("Karjat","Acne",5)
s.add(row2)
row2 = Frequency("Nagpur","Acne",45)
s.add(row2)
row2 = Frequency("Nashik","Acne",46)
s.add(row2)
row2 = Frequency("Delhi","Acne",554)
s.add(row2)
row2 = Frequency("Banglore","Acne",374)
s.add(row2)
row2 = Frequency("Amritsar","Acne",49)
s.add(row2)
row2 = Frequency("Chandigarh","Acne",394)
s.add(row2)
row2 = Frequency("Daman","Acne",64)
s.add(row2)
# row2 = Frequency("Amhemdabad","Acne",48)
# s.add(row2)
# row2 = Frequency("GandhiNagar","Acne",324)
# s.add(row2)
row2 = Frequency("Ratnagiri","Acne",94)
s.add(row2)
row2 = Frequency("Thane","Acne",10)
s.add(row2)
row2 = Frequency("Bhopal","Acne",6)
s.add(row2)
row2 = Frequency("Banglore","Acne",94)
s.add(row2)
row2 = Frequency("Manglore","Acne",74)
s.add(row2)
row2 = Frequency("Hyderabad","Acne",104)
s.add(row2)
row2 = Frequency("Tirupati","Acne",24)
s.add(row2)
row2 = Frequency("Kanpur","Acne",94)
s.add(row2)
row2 = Frequency("Amritapuri","Acne",84)
s.add(row2)
row2 = Frequency("Lucknow","Acne",84)
s.add(row2)
row2 = Frequency("Diu","Acne",84)
s.add(row2)
row2 = Frequency("Panaji","Acne",5)
s.add(row2)
row2 = Frequency("Kollam","Acne",35)
s.add(row2)

s.commit()
