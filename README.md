# Interview Master
- **Interview Master** is a CLI app designed to store user data, job fields, topics, and interview questions, offering a structured system for practicing interview questions across various job categories.
- Interview Master uses **SQLAlchemy** to manage the _interview_prep_ SQLite database.

## Table of Contents
1. [Installation](#installation)
2. [db Models](#db-models)
3. [CLI Commands](#cli-commands)
4. [Helper Functions](#helper-functions)
5. [Database](#database)
6. [Seeding Data](#seeding-data)
7. [Usage](#usage)
8. [License](#license)
   

# Installation
Follow these steps to set up the project:

## Step 1: Fork and Clone the Repository
- Fork the repository to your GitHub account.
- Clone the repository to your local machine:
   ```bash
   git clone https://github.com/BrendahKiragu/phase-3-project
   
   cd phase-3-project

## Step 2: Install Dependencies
Install the required Python dependencies using pipenv :
    ``` pipenv install ```

## Step 3: Activate the Virtual Environment
Start a shell within the pipenv environment:
    ``` pipenv shell ```
    
# db Models
The *lib/db/models.py* file defines the following data models (tables) in the interview_prep database:
 - `User`: Stores user information, including username and password.
 - `Job_field`: Represents job fields from which users get to practice questions related to a given field.
 - `Topic`: Defines individual topics under each job field.
 - `Question`: Defines interview questions tied to a specific topic, categorized under job fields.

# CLI Commands
The *lib/cli.py* contains the command-line interface (CLI) commands for you to interact with the app.
To interact with the app on the CLI:
1. Navigate to the lib directory: ``` cd lib/ ```
2. Run the CLI app: ``` python cli.py ```
 
You can interact with the app, such as creating your user account, add new quizs and practicing interview questions.

# Helper Functions
The *lib/helpers.py* file contains helper functions that run the CLI app. These functions handle tasks like:
 - displaying user options.
 - processing user input.
 - managing database interactions.

# Database
The SQLite database used by Interview Master is located at *lib/db/interview_prep.db*. This database contains the tables for users, job fields, topics, and interview questions as defined in the data models section.

# Seeding Data
To add data to the database for testing or demonstration purposes, you can use the lib/seed.py file. It contains functions to seed the database with sample data, as well as utility functions for querying the database.
  ### Seeding steps:
  1. Open *lib/seed.py*
  2. Uncomment the seed or query function call you'd like to run.
  3. In the terminal, run the following command to execute the seeding script:
      ``` python seed.py ```

 # Usage
 After setting up and activating the virtual environment, you can use the CLI to practice interview questions based on different job categories and topics. Here's how you can interact with the CLI:

1. **Create a User:** Start by creating your user account with a username and password.
2. **Select a Job Field:** Choose a job field you wish to focus on (e.g., software developer, data science, python developer).
3. **Pick a Topic:** After selecting a job field, you can choose a specific topic related to that field (e.g., algorithms, OOP).
4. **Answer Questions:** The app will present you with questions related to the chosen topic for practice.
5. **Create Quiz** Add questions to the existing topics or create your own topic with quizs.


# License Information
The Interview Master project is licensed under the MIT License.        
