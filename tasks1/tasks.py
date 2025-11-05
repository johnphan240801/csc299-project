import json
import os

DATA_FILE = "tasks.json"

def load_tasks():
    """Load tasks from JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("\nTask List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['title']} - {task.get('description', '')}")

def add_task():
    """Add a new task."""
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    tasks = load_tasks()
    tasks.append({"title": title, "description": description})
    save_tasks(tasks)
    print("Task added successfully!")

def search_tasks():
    """Search tasks by keyword."""
    keyword = input("Enter search keyword: ").lower().strip()
    tasks = load_tasks()
    results = [t for t in tasks if keyword in t['title'].lower() or keyword in t.get('description', '').lower()]
    if results:
        print("\nSearch Results:")
        for t in results:
            print(f"- {t['title']} ({t.get('description', '')})")
    else:
        print("No matching tasks found.")

def main():
    while True:
        print("\n--- Task Manager ---")
        print("1. List tasks")
        print("2. Add task")
        print("3. Search tasks")
        print("4. Quit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            list_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            search_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()


