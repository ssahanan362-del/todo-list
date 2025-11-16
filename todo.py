# To-Do List Application

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for t in tasks:
            file.write(t + "\n")

tasks = load_tasks()

while True:
    print("\n1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(i, task)

    elif choice == "2":
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        save_tasks(tasks)
        print("Task added.")

    elif choice == "3":
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            save_tasks(tasks)
            print("Task removed.")
        else:
            print("Invalid number.")

    elif choice == "4":
        print("Bye!,Come Again.")
        break

    else:
        print("Invalid choice.")