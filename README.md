# Interview Master
- **Interview Master** is a CLI app designed to store user data, job fields, topics, and interview questions, offering a structured system for practicing interview questions across various job categories.
- Interview Master uses **SQLAlchemy** to manage the _interview_prep_ SQLite database.

Table of Contents
1. [Installation](#installation)
2. [Database Models](#db.models)
3. [CLI Commands](#cli-py)
4. [Helper Functions](#helpers-py)
5. [Database](#interview_prep-db)
6. [Seeding Data](#seed-py)

# Installation
Follow these steps to set up the project:

## Step 1: Fork and Clone the Repository
- Fork the repository to your GitHub account.
- Clone the repository to your local machine:
   ```bash
   git clone https://github.com/BrendahKiragu/phase-3-project 
   cd interview-master

## Step 2: Install Dependencies
Install the required Python dependencies using pipenv (ensure that you have pipenv installed):
    ```bash
    pipenv install

## Step 3: Activate the Virtual Environment
Start a shell within the pipenv environment:
    ```bash
    pipenv shell

# Database Models
This file has classes that define the tables in the interview_prep database. These classes include:
 - `User`: Defines user information, including username and password.
 - `Job_field`: Represents a number of fields with topics from which user can practice quizzes on.
 - `Topic`: Defines individual topics related to a job field.
 - `Question`: Defines interview questions related to a specific topic.

# CLI Commands
Contains the command-line interface (CLI) function.
To run the app:
1. Navigate to the lib directory: cd lib/
2. On the terminal execute: python cli.py

# Helper Functions
Provides helper functions that run the CLI app.

# Database
This is the SQLite database that stores the data for this project. It contains the tables for the data models defined in db.models.

# Seeding Data
Contains functions that seed the database with sample data for testing the app. As well as database query functions
- To seed the database or run a query using seed.py:
   1. Uncomment the function calls in the file.
   2. Run in the terminal:
       ```bash
       python seed.py