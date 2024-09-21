#!/usr/bin/env python3
from db.models import User, myengine, Job_field, Question, Topic
from sqlalchemy.orm import sessionmaker
import json

session1 = sessionmaker(bind=myengine)
mysession = session1()

#CLI functions
def exit_program():
  """Exits from the CLI app"""
  print('*' * 100)
  print('Good Luck in your Interview')
  print('*' * 100)
  exit()

def login():
    """Logs in a user if the username and password exists in the database"""
    username = input("UserName: ")
    password = input("Password: ")
        
    try:
        user = mysession.query(User).filter_by(username=username).first()

        if user and user.password == password:
          print('=' * 100)
          print(f".........Glad to see you again 😁😁 {user.username}, What do you wanna do today?..........")
          print('=' * 100)
          return User
        else:
           print("Invalid credentials!")
           return None
    except Exception as exc:
        print("Error logging in, ", exc)
       
def show_jobs():
   """Shows all available jobs in the database"""
   try:
       jobs = mysession.query(Job_field).all() #gives a number to the list items
       if not jobs:
          print("No jobs available at the moment")
          return None

       for number, job in enumerate(jobs, start=1) : #adds numbering to the job field objects
           print(f"({number}) {job.job_name}")

       show_field_topics()
           
       selected_job = input("Select Topic(number) To Practice On: ")  
       print('=' * 100)  

       selected_job_number = int(selected_job) #converts selected_job input to integer

       if 1 <= selected_job_number <= len(jobs): #check if the selected input is within range 
          jobname = jobs[selected_job_number-1] #access the name of the list item
          take_quiz()
          return jobname
       else:
          print("Invalid Input! Select a valid job field from The list") 
   except Exception as exc:
      print("Error fetching job fields ", exc)

def take_quiz(topic_choosen=None):
    """CLI function for starting a quiz of the selected topic"""
    if topic_choosen is None:
        topic_choosen = input("Choose Topic number> ")

    try:
        # Fetches a topic based on the title input
        topic = mysession.query(Topic).filter_by(title=topic_choosen).first()

        if not topic:
            print("Topic not found!")
            return None

        # Fetches questions related to the selected topic
        questions = mysession.query(Question).filter_by(topic_id=topic.id).all()

        if questions:
            print('=' * 100)
            print(f"Starting quiz for topic: {topic.title}, in 3...2...1...")
            print("Wishing you all the best 🤝")
            print('=' * 100)
            score = 0
        else:
            print(f"Sorry, no available quizzes for {topic.title}")    

        for question in questions:
            print(f"Question: {question.question_text}")
            answers = json.loads(question.answers_text)
            for index, answer in enumerate(answers, start=1):
                print(f"{index}. {answer}")

            try:
                user_answer = int(input("Your answer (1-4)>_ "))

                if user_answer == question.correct_answer:
                    print("✅ Correct! ✅")
                    print('=' * 100)
                    score += 1
                else:
                    print(f"That doesn't seem right🤔🤔! The correct answer is: {question.correct_answer}")
                    print('=' * 100)
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 4.")

        # Displays final score
        print('=' * 100)
        print(f"Quiz finished! 👏👏👏👏 You scored: {score}/{len(questions)} 🥳🥳🥳🥳")
        print('=' * 100)
        print("What would you like to do next > ")
        from cli import menu2
        menu2()
    except Exception as exc:
        print("Error taking the quiz", exc)
   

#Class User functions
def create_user():
    """Adds a user to users table"""
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
    """Deletes user from users table"""
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
  

#Class Topic functions   
def list_topics():
    """lists all available topics from the database"""
    topics = mysession.query(Topic).all()  # Fetch all topics without filtering
    if not topics:
        print("No topics available.")
        return None

    # Display the topics with numbering
    for number, topic in enumerate(topics, start=1):
        print(f"({number}) {topic.title}")
    return topics

def show_field_topics():
    """Lists available topics for a selected job field"""

    while True:
        job_id =input("Select a job field (number) above to get started: ")
        print('=' * 100)
    
        try:
            topics = mysession.query(Topic).filter_by(job_field_id=job_id).all()
            if not topics:
                print("Invalid job field. Please select a number from the available job field number.")
                continue

            for index, topic in enumerate(topics, start=1):
                print(f"{index}.  {topic.title}")
            
            try:
                choice = int(input("Select a Topic (number) above to practice on: "))
                if 1 <= choice <= len(topics):               
                    choosen_topic = topics[choice-1]
                    take_quiz(choosen_topic.title)
                    break
                else:
                    print("Invalid choice, please select an existing topic.")    
                    continue
            except ValueError:
                print("Invalid input! Please enter a number.") 
            
        except Exception as exc:
            print("error occurred fetching topics: '{exc}'")

#Class Question functions
def create_quiz():
    """Adds a new question from cli app to questions table"""
    quiz = input("Type the quiz > ")
    answer1 = input("Answer 1: ")
    answer2 = input("Answer 2: ")
    answer3 = input("Answer 3: ")
    answer4 = input("Answer 4: ")
    print('=' * 100)
    
    while True:
        try:
            correct_answer = int(input("Enter the number of the correct answer (1-4): "))
            if 1 <= correct_answer <= 4:  # Validates the correct answer
                print(f"Correct answer set to {correct_answer}")
                break
            else:
                print("Correct answer must be between 1 and 4.") 
                
        except Exception as exc:
             print(f"Correct answer must be a value between 1 and 4 {exc}" )    
    
    # Shows job fields before selecting one
    jobs = mysession.query(Job_field).all()  # Retrieves all job fields
    if not jobs:
        print("Sorry no jobs available at the moment!!")
        return  # Exits if no jobs are available
    for number, job in enumerate(jobs, start=1):
        print(f"{number}. {job.job_name}")
    
    try:
        job_index = int(input("Select a job number above to add the quiz > "))
        print('=' * 100)
        if not (1 <= job_index <= len(jobs)):
            print("Invalid job number selected")
        
        selected_job = jobs[job_index - 1]  # fetches the selected job

        # Lists existing topics
        topics = list_topics()
        if not topics:
            # Allows user to create a new topic if none exist
            new_topic_title = input("No topics found. Enter a new topic title: ")
            print('=' * 100)
            new_topic = Topic(title=new_topic_title, job_field_id=selected_job.id) #create a new instance of Topic
            mysession.add(new_topic)
            mysession.commit()
            topic_id = new_topic.id #add to the Questions table column of topic_id
        else:
            # prompts the user to select an existing topic or add a new one
            topic_choice = input("Select a topic number above or type 'new' to add a new topic: ")
            print('=' * 100)
            if topic_choice.lower() == 'new':
                new_topic_title = input("Enter the new topic title: ")
                new_topic = Topic(title=new_topic_title, job_field_id=selected_job.id)
                mysession.add(new_topic)
                mysession.commit()
                topic_id = new_topic.id
            else:
                topic_index = int(topic_choice)
                if not (1 <= topic_index <= len(topics)):
                    raise ValueError("Invalid topic number selected.")
                selected_topic = topics[topic_index - 1]
                topic_id = selected_topic.id


        
        answers = [answer1, answer2, answer3, answer4]
        answers_json = json.dumps(answers)  # Converts answers to JSON format

        # Create the new question
        question = Question(
            question_text=quiz,
            answers_text=answers_json,  # Stores answers as JSON string
            correct_answer=correct_answer,  # Stores the index of the correct answer
            topic_id=topic_id  
        )

        # Adds and commits the new question to the database
        mysession.add(question)
        mysession.commit()

        print("Question created successfully!")
        print('=' * 100)

    except Exception as exc:
        print("Error creating question:", exc)
              