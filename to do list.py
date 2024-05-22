import json
from datetime import datetime

# File to store tasks
TASKS_FILE = 'tasks.json'

class Task:
    def __init__(self, title, priority='medium', due_date=None, completed=False):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

    def __repr__(self):
        return (f"Task(title='{self.title}', priority='{self.priority}', "
                f"due_date='{self.due_date}', completed={self.completed})")

def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks_data = json.load(file)
            return [Task(**task) for task in tasks_data]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump([task.__dict__ for task in tasks], file, indent=4)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for index, task in enumerate(tasks, start=1):
        status = '✓' if task.completed else '✗'
        due_date = task.due_date if task.due_date else 'No due date'
        print(f"{index}. [{status}] {task.title} (Priority: {task.priority}, Due: {due_date})")

def add_task(tasks):
    title = input("Enter the task title: ")
    priority = input("Enter the task priority (high, medium, low): ")
    due_date = input("Enter the due date (YYYY-MM-DD) or leave blank: ")
    due_date = due_date if due_date else None
    tasks.append(Task(title, priority, due_date))
    print("Task added.")

def remove_task(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            tasks.pop(task_number - 1)
            print("Task removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def mark_task_completed(tasks):
    display_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1].completed = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_task_completed(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == '__main__':
    main()
