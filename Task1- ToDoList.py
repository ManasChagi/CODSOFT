class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
        else:
            print("Invalid task index.")

    def show_tasks(self):
        print("\nTo-Do List:")
        for i, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else " "
            print(f"{i + 1}.{task['task']}[{status}] ")
        print()


todo_list = ToDoList()

while True:
    print("--------To-Do List-------")
    print("1. Add Task")
    print("2. Mark a Task as Completed")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        task = input("Enter task: ")
        todo_list.add_task(task)
    elif choice == "2":
        todo_list.show_tasks()
        task_index = int(input("Enter task index to mark as completed: ")) - 1
        todo_list.mark_completed(task_index)
    elif choice == "3":
        todo_list.show_tasks()
    elif choice == "4":
        print("Bye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

