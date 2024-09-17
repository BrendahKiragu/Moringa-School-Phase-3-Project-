from helpers import (
  exit_program, create_user, login,
  show_jobs, create_quiz,
  delete_user,
)

def app():
  while True:
    menu()
    choice = input("> ")
    if choice == "0":
       exit_program()
    elif choice == "1":
       create_user()
       menu2()
         
    elif choice == "2":
       login()   
       menu2() 
    elif choice == "5":
       delete_user()   
       

def menu():
  print("Welcome to Interview Master. How can we help you today? ") 
  print("0. Exit")
  print("1. CREATE AN ACCOUNT")
  print("2. LOGIN")
  print("5. DELETE MY ACCOUNT")

def menu2():
   while True:
       print("3. SELECT JOB FIELD")
       print("4. TAKE A QUIZ")
       print("5. CREATE A QUIZ")
       print("6. DELETE MY ACCOUNT")
       print("0. LOGOUT")
       
       choice = input("> ")
       if choice == "3":
          print("SELECT JOB FIELD.")
          show_jobs()
       elif choice == "4":
          create_quiz()
       elif choice == "5":
          delete_user()
       elif choice == "0":
          exit_program()      

if __name__ == "__main__":
     app()     