# file: ToDoList.py
# author: Hunter Risdon
# date: 2024-02-01
# description: This script implements a simple command-line to-do list application.
#              It allows users to add tasks, list tasks, and mark tasks as completed.

# 

tasks = []

def show_tasks():
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['name']} - {'Done' if task['completed'] else 'Not Done'}")

def add_task(task_name):
    tasks.append({"name": task_name, "completed": False})

# 
def complete_task(task_number):
    if task_number <= len(tasks) and task_number > 0:
        tasks[task_number - 1]['completed'] = True
    else:
        print("Invalid task number.")

# Prompts user with action
def get_user_choice():
    print("\nPlease select an option below: \n")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Complete a Task")
    print("4. Exit")
    return input("  Enter a number.")


# Main
while True:
    user_choice = get_user_choice()

    if user_choice == "1":
        task_name = input("Enter task name: ")
        add_task(task_name)
    elif user_choice == "2":
        show_tasks()
    elif user_choice == "3":
        task_number = int(input("Enter task number to complete: "))
        complete_task(task_number)
    elif user_choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please choose again.")