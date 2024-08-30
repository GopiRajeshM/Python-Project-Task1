import json
import os

class ToDoList:
    def __init__(self, filename='todo_list.json'):
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()
        print(f'Added task: {task}')

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            self.save_tasks()
            print(f'Deleted task: {removed_task["task"]}')
        else:
            print("Invalid task number.")

    def update_task(self, task_index, new_task):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["task"] = new_task
            self.save_tasks()
            print(f'Updated task to: {new_task}')
        else:
            print("Invalid task number.")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            self.save_tasks()
            print(f'Task marked as completed: {self.tasks[task_index]["task"]}')
        else:
            print("Invalid task number.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Pending"
                print(f'{i + 1}. {task["task"]} [{status}]')

    def menu(self):
        print("Welcome to the To-Do List Application")
        while True:
            print("\nMenu:")
            print("1. Add Task")
            print("2. Delete Task")
            print("3. Update Task")
            print("4. Complete Task")
            print("5. List Tasks")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                task = input("Enter the task: ")
                self.add_task(task)
            elif choice == '2':
                self.list_tasks()
                task_index = int(input("Enter task number to delete: ")) - 1
                self.delete_task(task_index)
            elif choice == '3':
                self.list_tasks()
                task_index = int(input("Enter task number to update: ")) - 1
                new_task = input("Enter the new task: ")
                self.update_task(task_index, new_task)
            elif choice == '4':
                self.list_tasks()
                task_index = int(input("Enter task number to mark as completed: ")) - 1
                self.complete_task(task_index)
            elif choice == '5':
                self.list_tasks()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo = ToDoList()
    todo.menu()
