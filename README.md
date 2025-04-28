# todolist using data type list
it is simple Todo List Magic Manager 

*def display_menu():
Defines a function to show the user the available options.

Displays a simple menu with 8 options — each one tied to a list operation.

tasks = ["Buy milk", "Submit report", "Call mom"]
priorities = [2, 1, 3]  # 1 = High, 3 = Low
Initializes two parallel lists:
tasks: stores the actual task strings.
priorities: stores priority levels for each task

extra_tasks = ["Water plants", "Read book"]
A second list to demonstrate joining two task lists.

while True:
Starts an infinite loop to keep the app running until the user exits.

display_menu()
choice = input("Choose an option (1-8): ")
Displays the menu and gets the user's choice.

Option 1: Show Tasks
Loops through the list using enumerate() to show task number and priority.
List concept used:
Looping
Accessing list items with tasks[i] and priorities[i]

Option 2: Add Task
Adds a new task and priority to both lists using .append().
List concept used:
Add items
List methods .append()

*Option 3: Edit Task
Changes an existing task by accessing it by index and updating the value.
List concept used:
Access items
Change items

Option 4: Remove Task
Removes a task and its priority using .pop(index) — safely removing by index.
List concept used:
Remove items
List method .pop()

*Option 5: Sort Tasks
Asks user if they want to sort alphabetically or by priority.

*Zips tasks and priorities into one list of tuples to sort them together.
Then sorts alphabetically by task name (x[0]).

*tasks, priorities = zip(*combined)
tasks, priorities = list(tasks), list(priorities)
Unzips the sorted tuples back into two lists.
List concept used:
Sort list
Tuple unpacking
Using .sort() method

elif sort_type == "2":
combined = list(zip(tasks, priorities))
combined.sort(key=lambda x: x[1])
tasks, priorities = zip(*combined)
tasks, priorities = list(tasks), list(priorities)
Same as above, but sorts by priority instead of name.


