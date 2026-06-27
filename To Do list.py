todo_list = []

def add_task(task):
    """Add a task to the global todo_list."""
    todo_list.append(task)
    print(f'Task "{task}" added.')  # f-string for clarity.  {task} is used to replace the actual task entered by the user.

def view_tasks():
    """Print all tasks, or a message when the list is empty."""
    if not todo_list:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for i, t in enumerate(todo_list, 1):  #Shows both index and task clearly.  No need to manage a separate counter variable.
            print(f'{i}. {t}')  #- {i} → Inserts the value of the variable i (usually the index or number).
                                #- {t} → Inserts the value of the variable t (usually the task or item).


def remove_task(task):
    """Remove a task if it exists; otherwise notify the user."""
    if task in todo_list:
        todo_list.remove(task)
        print(f'Task "{task}" removed from the list.')
    else:
        print(f'Task "{task}" not found in the list.')

def main():
    print("Welcome to To-Do List")
    while True:
        print("\n1. Add task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        try:   # Code that might cause an error
            choice = int(input("Enter your choice: "))
        except ValueError:  # Code that runs if there's an error
            print("Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            task = input("Enter the task: ").strip()  # ,strip() cleans up the extra spaces.
            if task:
                add_task(task)
            else:
                print("Empty task not added.")
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            task = input("Enter the task to remove: ").strip()
            if task:
                remove_task(task)
            else:
                print("Please enter a task name to remove.")
        elif choice == 4:
            print("Exiting... To-Do List. Goodbye!")
            sleepy_emoji = "\U0001F62A"
            print(sleepy_emoji)
            break
        else:
            print("Invalid choice. Please try again.")
            rolling_eyes = "\U0001F644"
            print(rolling_eyes)

if __name__ == "__main__":
    main()
#- ✅ The main() function runs only when the file is executed directly.
#- ❌ It won’t run if the file is imported into another script.
# __name__ is a special built-in variable.
