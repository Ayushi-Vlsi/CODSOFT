def show_menu():
    # Display the interactive user menu options
    print("\n--- TO DO LIST MANAGER ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Clear All Tasks")
    print("5. Exit")


def todo_list():
    tasks = []

    while True:
        show_menu()
        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            print("\nYour Tasks:")
            if tasks:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("No tasks added.")

        elif choice == "2":
            task = input("Enter a task: ").strip()
            tasks.append(task)
            print(f"'{task}' has been added to the list.")

        elif choice == "3":
            if not tasks:
                print("No tasks available to delete.")
                continue

            try:
                task_num = int(input("Enter the task number to delete: "))
                if 0 < task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"'{removed}' has been removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            tasks.clear()
            print("All tasks have been cleared.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


todo_list()
