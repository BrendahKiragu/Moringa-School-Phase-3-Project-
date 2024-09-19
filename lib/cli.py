#!/usr/bin/env python3
from helpers import (
  exit_program, create_user, login,
 show_jobs, create_quiz,  delete_user, take_quiz
)

def app():
    """CLI app"""
    while True:
      menu()
      choice = input("> ")
      if choice == "0":
         exit_program()
      elif choice == "1":
         create_user()
         menu2() #shows after an account is created
           
      elif choice == "2":
         if login():
             menu2() #shows if login is successful
         else:
            menu() #shows if login is unsuccessful
            print("Invalid Credentials. Confirm username or password is correct!")   
      elif choice == "5":
         delete_user()  
      else:
         print("Invalid choice, please try again.")    
       

def menu():
    """Starting menu when CLI app initializes"""
    print("______Welcome to Interview Master. How can we help you today?______ ") 
    print("0. Exit")
    print("1. CREATE AN ACCOUNT")
    print("2. LOGIN")
    print("5. DELETE MY ACCOUNT")

def menu2():
    """Shows up when a user is logged in to the app"""
    while True:
        print("3. Practice for an Interview")
        print("4. CREATE A QUIZ")
        print("5. DELETE MY ACCOUNT")
        print("0. LOGOUT")
        
        choice = input("> ")
        if choice == "3":
           print('=' * 100)
           show_jobs() #shows available job fields
           print('=' * 100)
           take_quiz()
               
        elif choice == "4":
           print('=' * 100)
           create_quiz()
        elif choice == "5":
           delete_user()
        elif choice == "0":
           print('LOGGING OUT...')
           break
        else:
           print("Invalid choice, please try again.")    

if __name__ == "__main__":
     app()     

     