"""
 Challenge: Terminal-Based Task List Manager

Create a Python script that lets users manage a to-do list directly from the terminal.

Your program should:
1. Allow users to:
   - Add a task
   - View all tasks
   - Mark a task as completed
   - Delete a task
   - Exit the app
2. Save all tasks in a text file named `tasks.txt` so data persists between runs.
3. Display tasks with an index number and a ✔ if completed.

Example menu:
1. Add Task  
2. View Tasks  
3. Mark Task as Completed  
4. Delete Task  
5. Exit

Example output:
Your Tasks:

Buy groceries||not_done
Finish Python project||done
Read a || book||not_done


Bonus:
- Prevent empty tasks from being added
- Validate task numbers before completing/deleting
"""

import os

TASK_FILE = "tasks.txt"

def load_tasks():
    tasks = []

    if (os.path.exists(TASK_FILE)):
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            for line in file:
                task, status = line.strip().rsplit("||", 1)
                tasks.append({"task": task, "done": status == "done"})

    return tasks
            
def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            status = "done" if task["done"] else "not_done"
            file.write(f"{task['task']}||{status}\n")

def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("Your Tasks:")
    for index, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else ""
        print(f"{index}. [{status}] {task['task']}")
    print()

def task_manager():
    tasks = load_tasks()

    while True:
        print("Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        match choice:
            case "1":
                task = input("Enter the task: ").strip()
                if task:
                    tasks.append({"task": task, "done": False})
                    save_tasks(tasks)
                    print("Task added successfully.")
                else:
                    print("Task cannot be empty.")
            case "2":
                display_tasks(tasks)
            case "3":
                display_tasks(tasks)
                try:
                    task_index = int(input("Enter the task number to mark as completed: ")) - 1
                    if 0 <= task_index < len(tasks):
                        tasks[task_index]["done"] = True
                        save_tasks(tasks)
                        print("Task marked as completed.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            case "4":
                display_tasks(tasks)
                try:
                    task_index = int(input("Enter the task number to delete: ")) - 1
                    if 0 <= task_index < len(tasks):
                        deleted_task = tasks.pop(task_index)
                        save_tasks(tasks)
                        print(f"Task deleted successfully: {deleted_task['task']}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            case "5":
                print("Exiting the app. Goodbye!")
                break
            case _:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    task_manager()

