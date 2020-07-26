from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import *
import os

path = os.path.join( os.path.dirname(os.path.abspath(__file__)), "static/sample_images//" )
print(path)
engine = create_engine('sqlite:///skiai.db')

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

'''
# Data ka format
Data(fname,lname,gender,age,Historyofpresentillness,
                    history1,history2,history3,history4,
                    symptom1,symptom2,symptom3,symptom4,symptom5,
                    Drugshistory,destination,model_pred,user_name,comment=None,status='0')

{'Acne': 0, 'Alopecia': 1, 'Normal Skin': 2, 'Tinea': 3}

< Add Status meaning here >
'''


case = Data("Nakul", "Somani", "male", "26",
    "India", "Maharashtra", "Mumbai",
    '','-','-','-','-','Itching','-','-','-','-','',
    path + 'acne-1.jpg',
    "Acne", "adi",
    "Wash you face regularly with clean waterand do not rub it. Avoid eating Oily food", 1
)
session.add(case)

case = Data("Prabha", "Ahuja", "female", "43",
    "India", "Maharashtra", "Pune",
    '','-','Hypertension','-','-','Itching','-','-','-','-','',
    path + 'acne-2.jpg',
    "Acne", "adi",
    "None", 0
)
session.add(case)

case = Data("Hrishikesh", "Jha", "male", "56",
    "India", "Maharashtra", "Pune",
    '','-','Hypertension','-','-','-','-','-','-','-','',
    path + 'alopecia-1.jpg',
    "Alopecia", "adi",
    "None", 0
)
session.add(case)

case = Data("Darpan", "Pal", "male", "24",
    "India", "Maharashtra", "Mumbai",
    'Early Hairfall','-','-','-','-','-','-','-','-','-','',
    path + 'alopecia-4.jpg',
    "Alopecia", "adi",
    "None", 0
)
session.add(case)

case = Data("Kunal", "Panth", "male", "22",
    "India", "Maharashtra", "Mumbai",
    '','-','-','-','-','-','-','-','-','-','',
    path + 'normal-1.jpg',
    "Normal Skin", "adi",
    "Your Skin is Healthy", 0
)
session.add(case)

case = Data("Mrunali", "Jadhav", "female", "27",
    "India", "Maharashtra", "Pune",
    '','-','-','-','-','-','-','-','-','-','',
    path + 'normal-2.jpg',
    "Normal Skin", "adi",
    "Your Skin is Healthy", 2
)
session.add(case)

case = Data("Vijay", "Deep", "male", "36",
    "India", "Maharashtra", "Mumbai",
    '','Diabetes','-','-','-','Itching','-','-','-','-','',
    path + 'tinea-1.jpg',
    "Tinea", "adi",
    "None", 0
)
session.add(case)

case = Data("Dheeraj", "Jodha", "male", "23",
    "India", "Maharashtra", "Pune",
    '','Diabetes','-','-','-','Itching','-','-','-','-','',
    path + 'tinea-3.jpg',
    "Tinea", "adi",
    "None", 0
)
session.add(case)


session.commit()
session.commit()

#Filling frequency table
results = engine.execute("select city, prediction, count(id) from data where prediction != 'Normal Skin' group by city, prediction")
for result in results:
    city, disease, freq = result
    session.add(Frequency(city, disease, freq))

session.commit()
session.commit()

