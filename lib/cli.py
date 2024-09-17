from helpers import (
  exit_program,
  create_user,
  login
)

def app():
  while True:
    menu()
    choice = input("> ")
    if choice == "0":
       exit_program()
    elif choice == "1":
       create_user()  
    elif choice == "2":
       login()    

def menu():
  print("Please select an option: ") 
  print("0. Exit")
  print("1. Create account")
  print("2. Login")

if __name__ == "__main__":
     app()     