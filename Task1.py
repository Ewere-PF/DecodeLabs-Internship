Tasks = []

while True:
    print("1. add task")
    print("2. view tasks")
    print("3. exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter the task: ")
        Tasks.append(task)
    elif choice == "2":
        print("Tasks:")
        for i, task in enumerate(Tasks, start=1):
            print(f"{i}. {task}")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")