task=[]
while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    c = int(input("enter your choice(1-4): "))
    if c == 1:
        t = input("Enter the task: ")
        task.append(t)
        print("Task added successfully.")
    elif c==2:
        if task==[]:
            print("No tasks available.")
        else:
            print("Your Tasks:")
            for i in task:
                print(i)
    elif c==3:
        if task==[]:
            print("No tasks to remove.")
        else:
            t=input("enter the task to remove: ")
            task.remove(t)
            print("Task removed successfully.")
    elif c==4:
        print("Exiting to-do list")
    