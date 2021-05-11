
from app import db, Users, Job

db.drop_all()
db.create_all()

testuser = Users(firstname='Grooty',surname='Toot') # Extra: this section populates the table with an example entry
# testcustomer = Customers('Jack','Parry','jp@hotmail.com','07777 777777','123 Street','LL199AA')
testjob = Job(customer_id=1,description='Do this job')
db.session.add(testuser)
db.session.add(testjob)
db.session.commit()