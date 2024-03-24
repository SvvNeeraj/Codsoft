class TodoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def delete_task(self, task_index):
        del self.tasks[task_index]
    def complete_task(self, task_index):
        self.tasks[task_index] += " (Completed)"
    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task}")
def main():
    todo_list = TodoList()
    while True:
        print("\n  To-Do List   ")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Delete Task")
        print("4. Show Tasks")
        print("5. Exit")
        choice = input("Enter your choice:")
        if choice == "1":
            task = input("Enter task:")
            todo_list.add_task(task)
            print("Task added successfully.")

        elif choice == "2":
            todo_list.show_tasks()
            task_index = int(input("Enter task number to mark as completed: ")) - 1
            if 0 <=task_index<len(todo_list.tasks):
                todo_list.complete_task(task_index)
                print("Task marked as completed.")
            else:
                print("Invalid task number.")
        elif choice == "3":
            todo_list.show_tasks()
            task_index = int(input("Enter task number to delete: ")) - 1
            if 0 <= task_index < len(todo_list.tasks):
                todo_list.delete_task(task_index)
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")
        elif choice == "4":
            print("\n*****Tasks*****")
            todo_list.show_tasks()

        elif choice == "5":
            print("Exiting... Thank you for using todolist Application")
            break

        else:
            print("Invalid choice. Please try again.")







if __name__ == "__main__":
    main()
