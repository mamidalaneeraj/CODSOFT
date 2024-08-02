print('welcome to the to-do list')
print('---------------------------')


# Creating a command-line To-Do List application
class ToDoList:
    def __init__(self):
        self.tasks = {}

    # Function to display tasks
    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("To-Do List:")
            for task, status in self.tasks.items():
                print(f"{task}: {status}")

    # Function to add task
    def add_task(self):
        task = input("Enter the task description: ").strip()
        if task:
            if task not in self.tasks:
                self.tasks[task] = "Not Started"
                print(f"Task '{task}' added!")
            else:
                print(f"Task '{task}' already exists.")
        else:
            print("Task description cannot be empty.")

    # Function to update task
    def update_task(self):
        task = input("Enter the task description to update: ").strip()
        if task in self.tasks:
            print("Available statuses: Not Started, In Progress, Completed")
            status = input("Enter new status: ").strip()
            if status in {"Not Started", "In Progress", "Completed"}:
                self.tasks[task] = status
                print(f"Task '{task}' updated!")
            else:
                print("Invalid status. Please choose from the available statuses.")
        else:
            print(f"Task '{task}' not found!")

    # Function to delete task
    def delete_task(self):
        task = input("Enter the task description to delete: ").strip()
        if task in self.tasks:
            del self.tasks[task]
            print(f"Task '{task}' deleted!")
        else:
            print(f"Task '{task}' not found!")

# Main function
def main():
    todo = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            todo.display_tasks()
        elif choice == "2":
            todo.add_task()
        elif choice == "3":
            todo.update_task()
        elif choice == "4":
            todo.delete_task()
        elif choice == "5":
            print("Thank you for using this to do application!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
