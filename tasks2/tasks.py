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
    """List all tasks with their status."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("\nTask List:")
    for i, task in enumerate(tasks, 1):
        status = "✅ Done" if task.get("completed") else "❌ Not Done"
        print(f"{i}. {task['title']} - {task.get('description', '')} [{status}]")

def add_task():
    """Add a new task."""
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    tasks = load_tasks()
    tasks.append({"title": title, "description": description, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

def mark_complete():
    """Mark a task as complete."""
    tasks = load_tasks()
    list_tasks()
    try:
        num = int(input("Enter task number to mark complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    """Delete a task by number."""
    tasks = load_tasks()
    list_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            deleted = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Deleted task: {deleted['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def search_tasks():
    """Search tasks by keyword."""
    keyword = input("Enter search keyword: ").lower().strip()
    tasks = load_tasks()
    results = [t for t in tasks if keyword in t['title'].lower() or keyword in t.get('description', '').lower()]
    if results:
        print("\nSearch Results:")
        for t in results:
            status = "✅" if t.get("completed") else "❌"
            print(f"- {t['title']} ({t.get('description', '')}) {status}")
    else:
        print("No matching tasks found.")

def main():
    while True:
        print("\n--- Task Manager v2 ---")
        print("1. List tasks")
        print("2. Add task")
        print("3. Mark task complete")
        print("4. Delete task")
        print("5. Search tasks")
        print("6. Quit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            list_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            search_tasks()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
