import os
import json
from datetime import datetime

# Function to load tasks from a JSON file
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        return tasks
    else:
        return {"tasks": []}

# Function to save tasks to a JSON file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)

# Function to display the current tasks
def display_tasks(tasks):
    if not tasks["tasks"]:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks["tasks"], start=1):
            print(f"{index}. {task['description']} - {task['created_at']}")

# Function to add a new task
def add_task(tasks, description):
    new_task = {"description": description, "created_at": str(datetime.now())}
    tasks["tasks"].append(new_task)
    save_tasks(tasks)
    print("Task added successfully.")

# Function to remove a task
def remove_task(tasks, index):
    if 1 <= index <= len(tasks["tasks"]):
        removed_task = tasks["tasks"].pop(index - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task['description']}' removed successfully.")
    else:
        print("Invalid task index.")

# Main function
def main():
    tasks = load_tasks()

    while True:
        print("\nTO-DO LIST APPLICATION")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            description = input("Enter task description: ")
            add_task(tasks, description)
        elif choice == "3":
            display_tasks(tasks)
            index = int(input("Enter the index of the task to remove: "))
            remove_task(tasks, index)
        elif choice == "4":
            print("Quitting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()