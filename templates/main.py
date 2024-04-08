tasks = []

# FUNCTION to add task
def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    tasks.append({"title": title, "description": description})
    print("Your task has been added!")


# FUNCTION to view task
def view_tasks():
    if tasks:
        print("Tasks: ")
        for idx, task in enumerate(tasks, start=1):  
            print(f"{idx}. Title: {task['title']}, Description: {task['description']}")
    else:
        print("No tasks found.")


# FUNCTION to update a task
def update_task():
    view_tasks()
    if tasks:
        task_index = int(input("Enter the index of the task to update: ")) - 1
        if 0 <= task_index < len(tasks):
            new_title = input("Enter new title (Enter to skip): ")
            new_description = input("Enter new description (Enter to skip): ")
            new_date_due = input("Enter new due date (Enter to skip): ")
            new_assignee = input("Enter new assignee (Enter to skip): ")
            if new_title:
                tasks[task_index]['title'] = new_title
            if new_description:
                tasks[task_index]['description'] = new_description
            print("Task updated successfully!")
        else:
            print("Invalid task ID. Please try again")
    else:
        print("No tasks available. Please add one first")


# FUNCTION to delete the task
def delete_task():
    view_tasks()
    if tasks:
        task_index = int(input("Enter the number of the task you want to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            print(f"Task '{deleted_task['title']}' deleted successfully!")
        else:
            print("Invalid task ID")
    else:
        print("No tasks available.")


# Main loop
while True:
    print("\nInteractive task manager")
    print("1. Add Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit Task")

    choice = input("Select an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid selection, please select 1-5.")
