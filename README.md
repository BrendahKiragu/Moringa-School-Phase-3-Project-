# Interview Master
- Interview Master is a CLI app that aims at helping job seekers prepare for interview by taking interactive quizzes in their job field.
- A user gets to create an account. Then selects their job field from a predefined list.
- The user then gets to choose between :  ["take a test"] vs ["create a quiz"]
  -For ["take a test"], the user takes a quiz test from their selected job_field. Once the user completes the quiz, they get to see their score  and the questions they got right.
 -For ["create a quiz"], the user can add a new quiz to their selected job_field, that will have questions, the multiple choices and correct answer to each question.
- Finally the user can select the "quit" to exit from the CLI app.

    ## The database schema:
 a) users (id, username, password) - will store the user details.

 b) job_fields (id, job_name) - will have job categories e.g. Data Science, DevOps.

 c) job_field_quizzes(id, title, job_field_id) - will have quizzes for each job_field.

 d) questions(id,  job_quiz_id, question_text) -  will have questions for each job_field_quiz.

 e) answers (id, question_id, answer_text, correct_answer) - will have multiple choice answers for each question.
