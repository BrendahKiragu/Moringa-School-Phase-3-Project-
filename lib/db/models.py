from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

Base = declarative_base()
myengine = create_engine('sqlite:///interview_prep.db')

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String(), nullable=False)
    password = Column(String(), nullable=False)
    
class Job_field(Base):
    __tablename__ = 'job_fields'    

    id = Column(Integer(), primary_key=True)
    job_name = Column(String())
    topics = relationship('Topic', backref=backref('job')) #job_field has many topics

class Topic(Base):
    __tablename__ = 'topics'    

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    job_field_id = Column(Integer(), ForeignKey('job_fields.id'))#belongs to job_field
    questions = relationship('Question', backref=backref('topic'))#topic has many questions

class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer(), primary_key=True)
    question_text = Column(String())
    answers_text = Column(String())#stores answers as a JSON string
    correct_answer = Column(Integer()) #stores the index of the correct answer
    topic_id = Column(Integer(), ForeignKey('topics.id'))#A question belongs to topic

Base.metadata.create_all(myengine)