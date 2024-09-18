from db.models import User, myengine, Job_field, Question, Topic
from sqlalchemy.orm import sessionmaker
import json

session1 = sessionmaker(bind=myengine)
mysession = session1()

#CLI functions
def exit_program():
  print('Good Luck in your Interview')
  exit()

def login():
    username = input("Enter your name: ")
    password = input("Enter your password: ")
        
    try:
        user = mysession.query(User).filter_by(username=username).first()

        if user and user.password == password:
          print(f"Glad to see you again {user.username}, What do you wanna do today?")
          return User
        else:
           print("Invalid credentials!")
           return None
    except Exception as exc:
        print("Error logging in, ", exc)
       
def show_jobs():
   try:
       jobs = mysession.query(Job_field).all() #gives a number to the list items
       if not jobs:
          print("No jobs available at the moment")
          return None

       for number, job in enumerate(jobs, start=1) : #adds numbering to the job field objects
           print(f"({number}) {job.job_name}")

       show_field_topics()
           
       selected_job = input("SELECT JOB BY NUMBER: ")    

       selected_job_number = int(selected_job) #converts selected_job input to integer

       if 1 <= selected_job_number <= len(jobs): #check if the selected input is within range 
          jobname = jobs[selected_job_number-1] #access the name of the list item
          take_quiz()
          return jobname
       else:
          print("Invalid Input! Select a valid job field from The list") 
   except Exception as exc:
      print("Error fetching job fields ", exc)

def take_quiz():
    topic_name = input("Enter the topic name to practice on: ")

    try:
        # Fetches a topic based on the title input
        topic = mysession.query(Topic).filter_by(title=topic_name).first()

        if not topic:
            print("Topic not found!")
            return None

        # Fetches questions related to the selected topic
        questions = mysession.query(Question).filter_by(topic_id=topic.id).all()

        if questions:
            print(f"Starting quiz for topic: {topic.title}")
            score = 0
        else:
            print(f"Sorry, no available quizes for this {topic.title}")    

        for question in questions:
            print(f"Question: {question.question_text}")
            answers = json.loads(question.answers_text) 
            for index, answer in enumerate(answers, start=1):
                print(f"{index}. {answer}")

            try:
                user_answer = int(input("Your answer (1-4)> _ "))

                if user_answer == question.correct_answer:
                    print("Correct!")
                    score += 1
                else:
                    print(f"That doesn't seem right! The correct answer is: {question.correct_answer}")
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 4.")

        # Display final score
        print(f"Quiz finished! You scored: {score}/{len(questions)}")
        
    except Exception as exc:
        print("Error taking the quiz", exc)
   

#Class User functions
def create_user():
    username = input("Enter your name: ").strip()
    password = input("Create your password: ").strip()

    try:
        user = User(username=username, password=password)
        mysession.add(user)
        mysession.commit()
        print(f"Welcome {user.username}. What do you want to do today?")
    except Exception as exc:
        print("Error creating account: ", exc)

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

def list_users():
    try:
        users = mysession.query(User).all()
        for user in users:
            print(f"User {user.id} : {user.username}")
            print("_" * 100)
    except Exception as exc:
        print("Error retrieving questions", exc) 

def find_user_by_name():
    query = input("Enter user name > ")

    try:
        user = mysession.query(User).filter_by(username=query).first()

        if user:
            print(f"User {user.id} : {user.username}")
        else:
            print("User not found!")    
    except Exception as exc:
        print("Error fetching job field", exc)

#Class JOB_FIELD functions
def create_job_field():
  name = input("Create job field > ") 

  try:
      job = Job_field(job_name=name) 
      mysession.add(job)
      mysession.commit()
      print(f"{job.job_name} added successfully.")
  except Exception as exc:
     print("Error creating job field ", exc)  

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

def list_job_fields():
    try:
        fields = mysession.query(Job_field).all()
        for field in fields:
            print(f"Job Field id: {field.id}")
            print(f"Job Name: {field.job_name}")
            print("_" * 100)
    except Exception as exc:
        print("Error retrieving questions", exc) 

def find_field_by_name():
    query = input("Enter job field name > ")

    try:
        field = mysession.query(Job_field).filter_by(job_name=query).first()

        if field:
            print(f"Job Field id: {field.id}")
            print(f"Job name: {field.job_name}")
        else:
            print("Field not found!")    
    except Exception as exc:
        print("Error fetching job field", exc) 


#Class Topicfunctions
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
        jobs = mysession.query(Job_field).all()
        print(f"Let's get your started with one of the available quizzes below.")

        for topic in topics:
            job = next((job for job in jobs if job.id == topic.job_field_id), None)
            print(f"Title: {topic.title}")
            print(f"Job field: {job.job_name if job else 'Not found'}")
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

def show_field_topics():
    job_id =input("Select Topic To Practice 0n > ")

    topics = mysession.query(Topic).filter_by(job_field_id=job_id).all()
    if topics:
        for index, topic in enumerate(topics, start=1):
            print(f"{index}:  {topic.title}")
 

    #     for topic in topics:

    #         print(f"{topic.title}")

    #  for number, job in enumerate(jobs, start=1) : #adds numbering to the job field objects
    #        print(f"({number}) {job.job_name}")
#Class Question functions
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