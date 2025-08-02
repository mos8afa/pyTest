def TaskManager():
    while True:
        print("__ TASK--MANAGER __")
        print("[1] ADD TASK      :")
        print("[2] VIEW TASKS    :")
        print("[3] DELETE TASK   :")
        print("[4] VIEW END TASK :")
        print("[5] End TASK      :")
        print("[6] Exit          :")
        try :
            choice = int(input("Please enter number of function: ").strip())
            if choice == 1:
                AddTask()
            elif choice == 2:
                ViewAllTasks()
            elif choice == 3:
                DeleteTask()
            elif choice == 4:
                ViewEndTasks()
            elif choice == 5:
                EndTask()
            elif choice == 6:
                print("Good bye")
                break
            else:
                
                print("Invalid input")
        except:
            print("Please enter a valid number")

def AddTask():
    while True:
        
        with open(r"D:\Python Basics\Projects\Tasks.txt", "r") as file:
            tasksList = [line.strip() for line in file.readlines()]
       
        new_task = input("Enter the task: ").strip().title()
        tasksList.append(new_task)
       
        with open(r"D:\Python Basics\Projects\Tasks.txt", "w") as file:
            for task in tasksList:
                file.write(task + "\n")

        print("Task has been added successfully")
        print("[1] Add another task...")
        print("[2] Back...")

        try:
            i = int(input("Enter the number of function: ").strip())
            if i == 1:
                continue
            elif i == 2:
                break
            else:
                print("Enter a valid input")
        except:
            print("Invalid number, going back...")
            break

def ViewAllTasks():
    if len(open(r"D:\Python Basics\Projects\Tasks.txt","r",encoding='utf-8').read()) >=1 :
        myTasks = open(r"D:\Python Basics\Projects\Tasks.txt","r")
        tasks = myTasks.readlines()
        for task in tasks:
            print(task)

    else:
        print("There is no tasks")
    input("Press enter to get back...")
    myTasks.close()

def DeleteTask():
    while True:
        try:
            if len(open(r"D:\Python Basics\Projects\Tasks.txt","r",encoding='utf-8').read()) >=1 :
                myTasks = open(r"D:\Python Basics\Projects\Tasks.txt","r")     
                content = [line.strip() for line in myTasks.readlines()]
                content.remove((input("Enter the task : ").strip()).title())     
                myTasks.close()

                myTasks = open(r"D:\Python Basics\Projects\Tasks.txt","w")
                for task in content:
                    myTasks.write(task+"\n")
                myTasks.close()  
           
                print("Task has been Deleted successfully")

            else:
                print("There is no tasks")
            print("[1] Delete another task...")
            print("[2] Back...")

            i = int(input("Enter the number of function: ").strip())

            if i == 1:
                continue

            elif i == 2:
                break

            else:
                print("Enter a valid input")

        except:
            print("Enter a Valid task name")          

def EndTask():
    while True:
        try:
            if len(open(r"D:\Python Basics\Tasks.txt","r",encoding='utf-8').read()) >=1:
                endTasks = open(r"D:\Python Basics\Projects\EndTasks.txt","r")
                endTaskList = [line.strip() for line in endTasks.readlines()]
                endTasks.close()
                endTask = (input("Enter the task : ").strip()).title()
                endTaskList.append(endTask)

                endTasks = open(r"D:\Python Basics\Projects\EndTasks.txt","w")
                for endTask in endTaskList :
                    endTasks.write(endTask +"\n")
                endTasks.close()

                myTasks = open(r"D:\Python Basics\Tasks.txt","r")     
                content = [line.strip() for line in myTasks.readlines()]
                content.remove(endTask)     
                myTasks.close()

                myTasks = open(r"D:\Python Basics\Tasks.txt","w")
                for task in content:
                    myTasks.write(task+"\n")
                myTasks.close()

                print("Task has been Done successfully")

            else:
                print("There is no tasks")
            print("[1] End another task...")
            print("[2] Back...")

            i = int(input("Enter the number of function: ").strip())

            if i == 1:
                continue

            elif i == 2:
                break

            else:
                print("Enter a valid input")

        except:
            print("Enter a Valid task name")

def ViewEndTasks():
    if len(open(r"D:\Python Basics\Projects\EndTasks.txt","r",encoding='utf-8').read()) >=1 :
        endTasks = open(r"D:\Python Basics\Projects\EndTasks.txt","r")
        Etasks = endTasks.readlines()
        for endTask in Etasks:
            print(endTask)
            
    else:
        print("There is no end tasks")
    input("Press enter to get back")

TaskManager()