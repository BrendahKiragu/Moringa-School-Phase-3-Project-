from helpers import (
  exit_program, create_user, login,
  take_quiz, create_quiz,
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
  print("1. Create account")
  print("2. Login")
  print("5. Delete my account")

def menu2():
   while True:
       print("3. Take A quiz")
       print("4. Create a quiz")
       print("5. Delete my account")
       print("0. Logout")
       
       choice = input("> ")
       if choice == "3":
          take_quiz()
       elif choice == "4":
          create_quiz()
       elif choice == "5":
          delete_user()
       elif choice == "0":
          exit_program()      

if __name__ == "__main__":
     app()     