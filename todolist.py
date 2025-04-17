
def display_menu():
    print("\n--- Todo List Magic Manager ---")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Edit task")
    print("4. Remove task")
    print("5. Sort tasks")
    print("6. Show high priority tasks")
    print("7. Backup and join with other list")
    print("8. Exit")

# Initial task list
tasks = ["Buy milk", "Submit report", "Call mom"]
priorities = [2, 1, 3]  # 1 = High, 3 = Low

# Another list to demonstrate join
extra_tasks = ["Water plants", "Read book"]

while True:
    display_menu()
    choice = input("Choose an option (1-8): ")

    if choice == "1":
        print("\n📋 Your Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task} (Priority: {priorities[i]})")

    elif choice == "2":
        task = input("Enter new task: ")
        priority = int(input("Enter priority (1-High, 3-Low): "))
        tasks.append(task)  # Add list item
        priorities.append(priority)
        print("Task added!")

    elif choice == "3":
        index = int(input("Enter task number to edit: ")) - 1
        if 0 <= index < len(tasks):
            new_task = input("Enter new task name: ")
            tasks[index] = new_task  # Change list item
            print("✏️ Task updated!")
        else:
            print("Invalid index.")

    elif choice == "4":
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)  # Remove list item
            priorities.pop(index)
            print(f"Removed: {removed}")
        else:
            print("Invalid index.")

    elif choice == "5":
        print("Sorting by (1) Alphabet or (2) Priority?")
        sort_type = input("Choose: ")
        if sort_type == "1":
            # Sort list alphabetically
            combined = list(zip(tasks, priorities))
            combined.sort(key=lambda x: x[0])
            tasks, priorities = zip(*combined)
            tasks, priorities = list(tasks), list(priorities)
        elif sort_type == "2":
            # Sort by priority
            combined = list(zip(tasks, priorities))
            combined.sort(key=lambda x: x[1])
            tasks, priorities = zip(*combined)
            tasks, priorities = list(tasks), list(priorities)
        print("Tasks sorted!")

    elif choice == "6":
        # List comprehension to show high priority only
        print("\n High Priority Tasks:")
        high_priority = [tasks[i] for i in range(len(tasks)) if priorities[i] == 1]
        for task in high_priority:
            print(f"- {task}")

    elif choice == "7":
        # Copy list
        backup = tasks.copy()
        # Join list
        tasks += extra_tasks
        priorities += [2] * len(extra_tasks)  # default medium priority
        print(" Extra tasks added. Backup created.")

        print("\n Backup of original tasks:")
        for task in backup:
            print(f"- {task}")

    elif choice == "8":
        print(" Exiting Todo List Manager. Goodbye!")
        break

    else:
        print(" Invalid choice. Please try again.")
