import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return [
        {"title": "Finish Python assignment", "completed": False},
        {"title": "Study for exam", "completed": False},
        {"title": "Practice coding", "completed": False}
    ]

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_menu():
    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")

def add_task(tasks):
    title = input("Enter task: ").strip()
    if title == "":
        print("Task cannot be empty!")
        return
    task = {"title": title, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available!")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✔️" if task["completed"] else "❌"
        print(f"{i}. {task['title']} [{status}]")

def mark_complete(tasks):
    if not tasks:
        print("No tasks to update!")
        return
    view_tasks(tasks)
    try:
        num = int(input("Enter task number: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked complete!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Enter a valid number!")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete!")
        return
    view_tasks(tasks)
    try:
        num = int(input("Enter task number: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid number!")
    except ValueError:
        print("Enter a valid number!")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose option (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()