# file: ToDoList.py
# author: Hunter Risdon
# date: 2024-02-01
# description: This script implements a simple command-line to-do list application.
#              It allows users to add tasks, list tasks, and mark tasks as completed.

# Imports
import json

# List to store tasks
tasks = []

# Function to display all tasks
def show_tasks():
    print("\nTasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['name']} - {'Done' if task['completed'] else 'Not Done'}")

# Function to add a task
def add_task(task_name):
    tasks.append({"name": task_name, "completed": False})

# Function to mark a task as completed
def complete_task(task_number):
    if task_number <= len(tasks) and task_number > 0:
        tasks[task_number - 1]['completed'] = True
    else:
        print("Invalid task number.")

# Function to prompt user for action
def get_user_choice():
    print("\nPlease select an option below: \n")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Complete a Task")
    print("4. Clear All Tasks")
    print("5. Exit")
    print("\nEnter a number:")
    return input()

# Function to save tasks to file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            if not task["completed"]: # Doesn't save completed tasks
                file.write(json.dumps(task) + "\n")

# Function to load tasks from file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(json.loads(line.strip()))
    except FileNotFoundError:
        pass # Previous task list does not exist

# Function to clear tasks
def clear_tasks():
    tasks.clear()

# Main
def main():
    print("Welcome to the To-Do List App!")
    load_tasks() # Load tasks from file
    while True:
        user_choice = get_user_choice()

        if user_choice == "1":
            task_name = input("\nEnter task name: ")
            add_task(task_name)
            print("\nTask added!")
        elif user_choice == "2":
            show_tasks()
        elif user_choice == "3":
            show_tasks()
            task_number = int(input("\nEnter task number to complete: "))
            complete_task(task_number)
        elif user_choice == "4":
            clear_tasks()
            print("Tasks cleared!")
        elif user_choice == "5":
            print("Saving...")
            save_tasks() # Save tasks before exiting
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()