
#====Login Section====

usernames = []
passwords = []
login = False

username = input("Enter your username: ")

password = input("Enter your password: ")

with open('user.txt','r')as file:
    for line in file:
        right_login = line.strip().split(", ")
        if username == right_login[0] and password == right_login[1]:

            print("Successful log in.")
            
            login = True

        if login == False:
            print("Incorrect details.")


if username =='admin' and password == 'adm1n':
        while True:
# Create a new menu to display for admin
            admin_menu = (input("""
Please select one of the following options:
r - register a new user
a - add task
va - view all tasks
vm - view my tasks
ds - display statistics 
e - exit

choice: """))

            if admin_menu == "r":
             
                    new_user = (input("Please enter a new username: "))
                    new_user_password = (input("Please enter a new password: "))
               
                 # Add a 'while loop' untill the condition is met(True).
                    confirm_new_password = input("Please confirm your password: ")

                    while True: 
                        if new_user_password != confirm_new_password:
                            print("Your passwords do not match!")
                            break
                   
                        with open ('user.txt', 'a')as user_file:
                            user_file.write("n")
                            user_file.write(new_user+", "+new_user_password)
                            break
                            
                    usernames.append(new_user)
                    passwords.append(new_user_password)


            elif admin_menu == "ds":
                # These varibles will only count the lines inside the 'txt' files,
                # but since I am storing every new task & user on a new line,
                # I can just count the lines for the desired results.
                tasks_num = 0
                users_num = 0

                with open("tasks.txt", "r") as task_file:
                    for line in task_file:
                        tasks_num += 1
                        print (f"\nTotal number of tasks: {tasks_num}")

                with open("user.txt", "r") as username:
                    for line in username:
                        users_num += 1
                        print (f"Total number of users: {users_num}")

 
            elif admin_menu == 'a':
                 #Asks the user for the username for who the task is given to
                    person_assigned = input("Please enter the username of the person who is assigned this task: ")
                    #Asks for the titel of the task
                    task_title = input("Please enter the titel of the task: ")
                    # Asks for the description for the task
                    task_description = input("Please enter the description of the task: ")
                    #Asks for the due date for when the task should be completed
                    due_date = input("Enter the due date for the task: ")
                    # Asks for the current date
                    current_date = input(str("Enter the current date: "))
                    # Task status
                    task_completion_status = 'No'
                   # All the info is then stored in the task.txt file 
                    with open('tasks.txt','a') as f:            
                        f.write(f'\n{person_assigned}, {task_title}, {task_description}, {due_date}, {current_date}, {task_completion_status}')

    
            elif admin_menu == 'va':
         
                with open('tasks.txt','r') as f:
                   for line in f:
                         splitted = line.split(",")

                         print(f"Task: {splitted[1]}")
                         print(f"Assigned to: {splitted[0]}")
                         print(f"Date assigned: {splitted[3]}")
                         print(f"Due date: {splitted[4]}")
                         print(f"Task complete: {splitted[5]}")
                         print(f"Task description: {splitted[2]}")
      
   
            elif admin_menu == 'vm':
                with open('tasks.txt','r')as f:
                    for line in f:
                        splitted2 = line.split(",")                       
                        print(f"Task: {splitted2[1]}")
                        print(f"Assigned to: {splitted2[0]}")
                        print(f"Date assigned: {splitted2[3]}")
                        print(f"Due date: {splitted2[4]}")
                        print(f"Task complete: {splitted2[5]}")
                        print(f"Task description: {splitted2[2]}")

            elif admin_menu == 'e':
                print('Goodbye!!!')
                exit()

            else:
                print("You have made a wrong choice, Please Try again")

if login == True:
  
        while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
            menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
choice:  ''').lower()
 

            if menu == 'r':
                print("Only an Admin can register a user")
                exit()
           
            elif menu == 'a':
                 #Asks the user for the username for who the task is given to
                    person_assigned = input("Please enter the username of the person who is assigned this task: ")
                    #Asks for the titel of the task
                    task_title = input("Please enter the titel of the task: ")
                    # Asks for the description for the task
                    task_description = input("Please enter the description of the task: ")
                    #Asks for the due date for when the task should be completed
                    due_date = input("Enter the due date for the task: ")
                    # Asks for the current date
                    current_date = input(str("Enter the current date: "))
                    task_completion_status = "No"    
                    # All the info is then stored in the task.txt file
                    with open('tasks.txt','a') as f:
                        f.write(f'\n{person_assigned}, {task_title}, {task_description}, {due_date}, {current_date}, {task_completion_status}')
         
            elif menu == 'va':
         
                with open('tasks.txt','r') as f:
                   for line in f:
                         splitted = line.split(",")
                
                         print(f"Task: {splitted[1]}")
                         print(f"Assigned to: {splitted[0]}")
                         print(f"Date assigned: {splitted[3]}")
                         print(f"Due date: {splitted[4]}")
                         print(f"Task complete: {splitted[5]}")
                         print(f"Task description: {splitted[2]}")
    
            elif menu == 'vm':
                with open('tasks.txt','r')as f:
                    for line in f:
                        splitted2 = line.split(",")
                        

                        print(f"Task: {splitted2[1]}")
                        print(f"Assigned to: {splitted2[0]}")
                        print(f"Date assigned: {splitted2[3]}")
                        print(f"Due date: {splitted2[4]}")
                        print(f"Task complete: {splitted2[5]}")
                        print(f"Task description: {splitted2[2]}")

            elif menu == 'e':
                print('Goodbye!!!')
                exit()

            else:
                print("You have made a wrong choice, Please Try again")









 





                
               
          





                        
                     









