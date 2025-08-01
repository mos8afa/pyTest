myTasks = []
endTasks = []

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
        myTasks.append((input("Enter the task: ").strip()).title())
        print("Task has been added successfully")
        print("[1] Add another task...")
        print("[2] Back...")
        i = int(input("Enter the number of function: ").strip())
        if i == 1:
            continue
        elif i == 2:
            break
        else:
            print("Enter a valid input")    

def ViewAllTasks():
    if len(myTasks) >=1:
        for task in myTasks:
            print(task)
    else:
        print("There is no tasks")
    input("Press enter to get back...")

def DeleteTask():
    while True:
        try:
            if len(myTasks) >= 1:
                myTasks.remove((input("Enter task name : ").strip()).title())
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
            if len(myTasks) >= 1:
                endTask = input("Enter the task : ").strip().title()
                endTasks.append(endTask)
                myTasks.remove(endTask)
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
    if len(endTasks) >=1:
        for endTask in endTasks:
            print(endTask)
    else:
        print("There is no end tasks")
    input("Press enter to get back")

TaskManager()