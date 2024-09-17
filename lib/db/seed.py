#!/usr/bin/env python3

from db.models import myengine, Job_field, Topic
from sqlalchemy.orm import sessionmaker
from faker import Faker

faker = Faker()

if __name__ == '__main__':
    Session = sessionmaker(bind = myengine)
    mysession = Session()
   
# print("...seeding database")   

# job1 = Job_field("Python developer")
# topic1 = Topic("Data Types", job1)

# mysession.add(job1)
# mysession.commit()