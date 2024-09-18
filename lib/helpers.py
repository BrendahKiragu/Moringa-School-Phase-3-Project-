from db.models import User, myengine, Job_field, Question
from sqlalchemy.orm import sessionmaker
import json

session1 = sessionmaker(bind=myengine)
mysession = session1()

def exit_program():
  print('Good Luck in your Interview')
  exit()

def take_quiz():
   
   pass

def create_quiz():
   quiz = input("Type the quiz > ")
   answer1 = input("Answer 1: ")
   answer2 = input("Answer 2: ")
   answer3 = input("Answer 3: ")
   answer4 = input("Answer 4: ")
   correct_answer = int(input("Enter the number of the correct answer(1-4) "))

   try:
       answers = [answer1, answer2, answer3, answer4]
       answers_json = json.dumps(answers)

       question = Question(
            question_text=quiz,
            answers_text=answers_json,  # Store answers as JSON string
            correct_answer=correct_answer  # Store the index of the correct answer
        )
       
       mysession.add_all(question) #adds quiz to questions table
       mysession.commit()

       print("Question created successfully!")

   except Exception as exc:
      print("Error creating question", exc)   
        
def delete_quiz():
    query = int(input("Enter Quiz id: "))

    quiz_to_delete = mysession.query(Question).filter_by(id=query).first()
    if quiz_to_delete:
       try:
           mysession.delete(quiz_to_delete)
           mysession.commit()
           print("Quiz Deleted")
       except Exception as exc:
           print("Error deleting question...", exc)
    else:
       print("Question does not exist!")
    
# def create_answers():
#    answers = []

#    try:
#       for i in range(1, 5):
#          answer = input(f"type answer {i} > ") 
#          answers.append(Answer(answer_text=answer))

#       mysession.add_all(answers)
#       mysession.commit()
#       print("Answers added successfully!")
#    except Exception as exc:
#       print("Error creating answers", exc)   

def show_jobs():
  #  selected_job = input("> ")
   try:
       jobs = mysession.query(Job_field).all() #gives a number to the list items
       if not jobs:
          print("No jobs available at the moment")

       for number, job in enumerate(jobs, start=1) : #adds numbering to the job field objects
           print(f"({number}) {job.job_name}")
           
       selected_job =input("SELECT JOB BY NUMBER: ")    

       selected_job_number = int(selected_job) #converts selected_job input to integer

       if 1 <= selected_job_number <= len(jobs): #check if the selected input is within range 
          jobname = jobs[selected_job_number-1] #access the name of the list item
          print(f"selected {jobname.job_name}")
       else:
          print("Invalid Input! Select a valid job field from The list") 
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
