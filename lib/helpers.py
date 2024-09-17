from db.models import User, myengine, Job_field
from sqlalchemy.orm import sessionmaker

session1 = sessionmaker(bind=myengine)
mysession = session1()

def exit_program():
  print('Good Luck in your Interview')
  exit()

def take_quiz():
   
   pass

def create_quiz():
   pass

def show_jobs():
  #  selected_job = input("> ")
   try:
       for job in mysession.query(Job_field).all():
          print(job)
       
   except Exception as exc:
      print("invalid input ", exc)

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
          print(f"Glad to see you again {user.username}, What do you wanna do today?")
        else:
          raise ValueError("Invalid username or password!")  
    except Exception as exc:
        print("Error logging in, ", exc)

#def delete user()
def delete_user():
    username = input("Enter user's name: ")
    password = input("Enter your password: ")

    user_to_delete = mysession.query(User).filter_by(username=username).first()
    
    if user_to_delete and user_to_delete.password == password:
        try:     
            mysession.delete(user_to_delete)
            mysession.commit()
            print(f"Dear {user_to_delete.username}, your account has been deleted.")  
        except Exception as exc:
            print("Error occurred deleting the account, try again!", exc)  
    else:
       print("User account or password incorrect")             

#def list_users()

#Class JOB_FIELD
#def create job_field()
def create_job_field():
  name = input("Create job field > ") 

  try:
      job = Job_field(job_name=name) 
      mysession.add(job)
      mysession.commit()
      print(f"{job.job_name} added successfully.")
  except Exception as exc:
     print("Error creating job field ", exc)     
#def delete job_field()
def delete_job_field():
    name_ = input("Enter Job field to delete > ")

    try:
        field_to_delete = mysession.query(Job_field).filter_by(job_name=name_).first()
        if field_to_delete:
                mysession.delete(field_to_delete)
                mysession.commit()
                print(f"Job_field {name_} deleted")
        else:
           print("Job field not found")        
    except Exception as exc:
      print("Error deleting the job field ", exc)      
#def list_jobs_fields()
#def find_by_id()
def find_by_id():
   pass

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