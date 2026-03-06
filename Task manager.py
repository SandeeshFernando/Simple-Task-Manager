#Author- D.U.I Sandeesh Fernando (W2152931)
#date= 30th March of 2025
#Coursework for Stage 1 CRUD operations and Creating a task manager for daily routuine and tasks

#List to store tasks
tasks = []

#File to save
FILENAME = "save_file.txt"

#----CRUD Functions-----
# Function to add a task
def add_task():
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    priority = input("Enter task priority (High/Medium/Low): ")
    due_date = input("Enter task due date (DD-MM-YYYY): ")

    #Input correction
    if not name or not description:
        print('Error: Name and description cannot be empty!')
    if priority not in ["High" ," Medium" , "Low"]:
        print("Error; invaild priority, Use High/Medium/Low")
        return
    
    task = [name, description, priority, due_date]
    tasks.append(task)
    print("Task added successfully!\n")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks to Show.")
    else:
        for index, task in enumerate(tasks):
            print(f"Task {index + 1}: {task}")
        print("\n")

# Function to update a task
def update_task():
    view_tasks()
    try:
        task_index = int(input("Enter task number to update: ")) - 1
        if 0 <= task_index < len(tasks):
            new_name = input("Enter new task name: ")
            new_description = input("Enter new description : ")
            new_priority = input("Enter new priority : ")
            new_due_date = input("Enter new due date: ")
            
            if new_name:
                tasks[task_index][0] = new_name
            if new_description:
                tasks[task_index][1] = new_description
            if new_priority:
                tasks[task_index][2] = new_priority
            if new_due_date:
                tasks[task_index][3] = new_due_date
                print("Task updated successfully!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")
        

# Function to delete a task
def delete_task():
    view_tasks()
    try:
        task_index = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks.pop(task_index)
            print("Task deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    load_tasks_from_file()  # Load tasks on startup
    while True:
        print("\n===== Task Manager Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Save and Exit")  # Changed from "Exit" to "Save and Exit"

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                update_task()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                save_tasks_to_file()  # Save tasks before exiting
                print("Exiting program.")
                break
            else:
                print("Invalid option. Please choose again.")
        except ValueError:
            print("Please enter a valid number.")
            
# Run the program
if __name__ == "__main__":
    main()

def save_tasks_to_file():
    """Save tasks to save_file.txt"""
    try:
        with open(FILENAME, "w") as file:
            for task in tasks:
                file.write(",".join(task) + "\n")  # Write tasks as CSV lines
        print("Tasks saved successfully!")
    except Exception as e:
        print(f"Error saving tasks: {e}")

def load_tasks_from_file():
    """Load tasks from save_file.txt"""
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                task_data = line.strip().split(",")
                if len(task_data) == 4:  # Only load valid tasks
                    tasks.append(task_data)
        print("Tasks loaded from file!")
    except FileNotFoundError:
        print("No existing tasks file. Starting fresh.")
    except Exception as e:
        print(f"Error loading tasks: {e}")
