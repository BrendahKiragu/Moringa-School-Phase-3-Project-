from db.models import User, myengine
from sqlalchemy.orm import sessionmaker

session1 = sessionmaker(bind=myengine)
mysession = session1()

def exit_program():
  print('Good Luck in your Interview')
  exit()

# Class USER 
#def create user()
def create_user():
  username = input("Enter your name: ")
  password = input("Create your password: ")

  try:
    user = User(username=username, password=password)
    mysession.add(user)
    mysession.commit()
    print(f"Welcome {user.username}. What do you want to do today?")
  except Exception as exc:
    print("Error creating account: ", exc)  

def login():
    username = input("Enter your name: ")
    password = input("Enter your password: ")
    try:
        user = mysession.query(User).filter_by(username=username).first()
        if user and user.password == password:
          print(f"welcome back, user {user.username}")
        else:
          raise ValueError("Invalid username or password!")  
    except Exception as exc:
        print("Error logging in, ", exc)
#def delete user()
#def list_users()

#Class JOB_FIELD
#def create job_field()
#def delete job_field()
#def list_jobs_fields()
#def find_by_id()

#Class Topic
#def create topic
#def delete topic
#def list_topics()
#def find_by_id

#Class Question
#def create questions
#def delete question
#def list_questions()
#def find_by_id

#Class Answer
#def create answers
#def delete answers
#def list_answers()
#def find_by_id

#def list_topic_questions()
#def list_question_answers()
#def list_job_field_topics()