from db.models import User, myengine, Job_field, Question, Topic
from sqlalchemy.orm import sessionmaker
import json

session1 = sessionmaker(bind=myengine)
mysession = session1()

def exit_program():
  print('Good Luck in your Interview')
  exit()

def take_quiz():
   
   pass    

def show_jobs():
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
      print("Error fetching job fields ", exc)

# Class USER 
#def create user()
def create_user():
    username = input("Enter your name: ").strip()
    password = input("Create your password: ").strip()

    # Input validation
    if not username:
        print("Username must not be empty!")
        return  # Exit the function if validation fails

    if len(password) < 4:
        print("Password must be at least 4 characters long!")
        return  # Exit the function if validation fails

    # Attempt to create the user
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
    name_ = input("Enter Job field name to delete > ")

    try:
        field_to_delete = mysession.query(Job_field).filter_by(job_name=name_).first()
        if field_to_delete:
                mysession.delete(field_to_delete)
                mysession.commit()
                print(f"Job_field {name_} deleted")
        else:
           print(f"Job field '{name_}' not  found")        
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
def create_topic():
    name = input("Create topic title > ")
    field_id = input("Enter job field id > ")

    try:
        topic = Topic(title=name, job_field_id=field_id)
        mysession.add(topic)
        mysession.commit()
        print(f"{topic.title} created successfully")
    except Exception as exc:
        print("Error creating topic", exc)    
 
def delete_topic():
    try:
        query = input("Enter Topic to delete: ")
        del_topic = mysession.query(Topic).filter_by(id=query).first()

        if del_topic:
            mysession.delete(del_topic)
            mysession.commit()
            print("Topic delete successfully.")

    except Exception as exc:
        print("Error deleting topic", exc)    

def list_topics():
    try:
        topics = mysession.query(Topic).all()
        for topic in topics:
            print(f"Topic id: {topic.id}")
            print(f"Title: {topic.title}")
            print(f"Job field id: {topic.job_field_id}")
            print("_" * 100)
    except Exception as exc:
        print("Error retrieving questions", exc) 

def find_topic_by_name():
    query = input("Enter topic name > ")

    try:
        topic = mysession.query(Topic).filter_by(title=query).first()

        if topic:
            print(f"Title: {topic.title} belongs to Job field {topic.job_field_id}")
        else:
            print("Topic not found!")    
    except Exception as exc:
        print("Error fetching topic", exc)    

#adds question to table questions
def create_quiz():
   quiz = input("Type the quiz > ")
   answer1 = input("Answer 1: ")
   answer2 = input("Answer 2: ")
   answer3 = input("Answer 3: ")
   answer4 = input("Answer 4: ")
   topic_id = int(input("Enter the topic ID for this question > "))

   try:
       correct_answer = int(input("Enter the number of the correct answer(1-4) "))
       
       if not (1 <= correct_answer <= 4): #validates the correct answer
          raise ValueError("Correct answer must be between 1 and 4.")
       
       answers = [answer1, answer2, answer3, answer4]
       answers_json = json.dumps(answers)

       question = Question(
            question_text=quiz,
            answers_text=answers_json,  # Store answers as JSON string
            correct_answer=correct_answer,  # Store the index of the correct answer
            topic_id=topic_id
        )
       
       mysession.add(question) #adds quiz to questions table
       mysession.commit()

       print("Question created successfully!")

   except Exception as exc:
      print("Error creating question", exc)   
        
#deletes question from database
def delete_quiz():
    try:
        query = int(input("Enter Quiz ID to delete: "))
        quiz_to_delete = mysession.query(Question).filter_by(id=query).first()
        
        if quiz_to_delete:
            mysession.delete(quiz_to_delete)
            mysession.commit()
            print("Quiz deleted successfully.")
        else:
            print("Question does not exist!")
    
    except Exception as exc:
        print("Error deleting question:", exc)

#lists all questions
def list_questions():
    try:
        questions = mysession.query(Question).all()
        for question in questions:
            print(f"Question id: {question.id}")
            print(f"Question: {question.question_text}")
            print(f"Answers: {json.loads(question.answers_text)}")
            print(f"Correct Answer Index: {question.correct_answer}")
            print("_" * 100)
    except Exception as exc:
        print("Error retrieving questions", exc)        

#finds questions by their id
def find_question_by_id():
    question_id = input("Search quiz by id > ")

    try:
        quiz = mysession.query(Question).filter_by(id=question_id).first()
        if quiz:
            print(f"ID: {quiz.id}")
            print(f"Question: {quiz.question_text}")
            print(f"Answers: {json.loads(quiz.answers_text)}")  # Convert JSON string back to list
            print(f"Correct Answer Index: {quiz.correct_answer}")
        else:
            print("Question not found.")

    except Exception as exc:
        print("Error retrieving quiz", exc)    