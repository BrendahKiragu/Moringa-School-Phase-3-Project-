#!/usr/bin/env python3
from helpers import mysession, delete_user
from db.models import Topic, Job_field, User, Question
import json


print("...seeding database")   

#Class TOPIC functions
def create_topic():
    """Creates and adds a new topic to the database"""
    name = input("Create topic title > ")
    field_id = input("Enter job field id > ")

    try:
        topic = Topic(title=name, job_field_id=field_id)
        mysession.add(topic)
        mysession.commit()
        print(f"{topic.title} created successfully")
    except Exception as exc:
        print("Error creating topic", exc) 
# create_topic()        

def delete_topic():
    """Deletes a topic from database"""
    try:
        query = input("Enter Topic to delete: ")
        del_topic = mysession.query(Topic).filter_by(title=query).first()

        if del_topic:
            mysession.delete(del_topic)
            mysession.commit()
            print(f"'{del_topic.title}' topic delete successfully.")

    except Exception as exc:
        print("Error deleting topic", exc)      
# delete_topic()
   
def find_topic_by_name():
    """finds topic by name"""
    query = input("Enter topic name > ")

    try:
        topic = mysession.query(Topic).filter_by(title=query).first()

        if topic:
            print(f"Title: {topic.title} belongs to Job field {topic.job_field_id}")
        else:
            print("Topic not found!")    
    except Exception as exc:
        print("Error fetching topic", exc)
# find_topic_by_name()  
      

#Class JOB_FIELD functions
def create_job_field():
  """adds a new job field to the database"""
  name = input("Create job field > ") 

  try:
      job = Job_field(job_name=name) 
      mysession.add(job)
      mysession.commit()
      print(f"{job.job_name} added successfully.")
  except Exception as exc:
     print("Error creating job field ", exc)     
# create_job_field()           

def find_field_by_name():
    """finds job field by name"""
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
# find_field_by_name()

def list_job_fields():
    """lists all job fields"""
    try:
        fields = mysession.query(Job_field).all()
        for field in fields:
            print(f"Job Field id: {field.id}")
            print(f"Job Name: {field.job_name}")
            print("_" * 100)
    except Exception as exc:
        print("Error retrieving questions", exc) 
# list_job_fields()   

def delete_job_field():
    """deletes a job field from database"""
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
# delete_job_field()   


# class USER functions
def find_user_by_name():
    """finds user by name"""
    query = input("Enter user name > ")

    try:
        user = mysession.query(User).filter_by(username=query).first()

        if user:
            print(f"User {user.id} : {user.username}")
        else:
            print("User not found!")    
    except Exception as exc:
        print("Error fetching job field", exc)
# find_user_by_name()        

def list_users():
    """Lists all users available in users table"""
    try:
        users = mysession.query(User).all()
        for user in users:
            print(f"User {user.id} : {user.username}")
            print("_" * 100)
    except Exception as exc:
        print("Error retrieving questions", exc)  
# list_users()   
# delete_user()    


#class QUESTIONS functions
def find_question_by_id():
    """Finds question by id"""
    question_id = input("Search quiz by id > ")

    try:
        quiz = mysession.query(Question).filter_by(id=question_id).first()
        if quiz:
            print(f"ID: {quiz.id}")
            print(f"Question: {quiz.question_text}")
            print(f"Answers: {json.loads(quiz.answers_text)}")  # Converts JSON string back to list
            print(f"Correct Answer Index: {quiz.correct_answer}")
        else:
            print("Question not found.")

    except Exception as exc:
        print("Error retrieving quiz", exc)  
# find_question_by_id()

#lists all questions
def list_questions():
    """Lists all questions available in the database"""
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
# list_questions()          