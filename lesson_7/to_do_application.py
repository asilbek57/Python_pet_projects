class Task:
    def __init__(self, task_id, title, description, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return(f"{self.task_id}, {self.title}, {self.description}, {self.status}")
    
    def to_dict(self):
        return {
            "Task_ID" : self.task_id,
            "Title" :self.title,
            "Description": self.description,
            "Status" : self.status,
            }
    
    #now converting plain lists from dictionary into actual objects that TaskManager can use
    #@classmethod is to work on the class itself, not just object like t.method

    @classmethod
    def from_dict(cls, data):
        return cls(data["task_id"], data["title"], data["description"], data["status"])
    

class CSVStorage:
    def __init__(self, filename):
        self.filename = filename

    def save(self, tasks):
        import csv
        with open(self.filename, 'w', newline = '') as f:
            writer = csv.writer(f)
            for task in tasks.values():
                writer.writerow([task.task_id, task.title, task.description, task.status])
    
    def load(self):
        import csv
        tasks ={}
        try:
            with open("tasks.txt", 'r', newline = '') as f:
                reader = csv.reader(f)
                for line in reader:
                    task_id, title, description, status = line
                    tasks[task_id] = Task(task_id,title, description, status)
        except FileNotFoundError:
            print("Such file does not exist!")
        return tasks

class JSONStorage:
    def __init__(self, filename):
        self.filename = filename

    def save(self, tasks):
        import json
        with open('tasks.txt', 'w') as f:
            json.dump([t.to_dict() for t in tasks.values()], f)
    
    def load(self):
        import json
        tasks = {}
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
            for item in data:
                t = Task.from_dict(item)
                tasks[t.task_id] = t
        except FileNotFoundError:
            pass
        return tasks

class Task_Manager:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = self.storage.load()

    def add(self):
        task_id = input("Enter ID of the task: ")
        title = input("Enter name: ")
        description=input("Enter description: ")
        status = input("Enter status (Pending/In progress/Competed): ")
        self.tasks[task_id] = Task(task_id, title, description, status)
        print("Task has been added!")

    def view(self):
        for n in self.tasks.values():
            print(n)

    def update(self):
        q = input("Enter ID: ")
        if q in self.tasks:
            idd = self.tasks[q]
            idd.title = input("Enter title: ")
            idd.description = input("Enter description")
            idd.status = input("Enter status (Pending, In progress, Completed)")
            
            print("Task has been updated")
        else:
            print("No such task")
        
    def delete(self):
        q = input("Enter ID: ")
        if q in self.tasks:
            del self.tasks[q]
            
            print("Task has been deleted")
        else:
            print("No such task")

    def filtering(self):
        ask = input("Search by status: ")
        matches = [task for task in self.tasks.values() if task.status == ask]
        if matches:
            for task in matches:
                print(task)
        else:
            print("No tasks with such status")

    def save_tasks(self):
        self.storage.save(self.tasks)
        print("Tasks saved successfully.")

    def load_tasks(self):
        self.tasks = self.storage.load()
        print("Tasks loaded successfully.")

    def menu(self):
        while True:
            print("""Welcome to the To-Do Application!
                    1. Add a new task
                  2. View All tasks
                  3. Update a task
                  4. Delete a task
                  5. Filter tasks by status
                  6. Save tasks
                  7. Load tasks
                  8. Exit
                  """)
            ch = input("Enter your choice: ")
            if ch == '1':
                self.add()
            elif ch =='2':
                self.view()
            elif ch =='3':
                self.update()
            elif ch =='4':
                self.delete()
            elif ch =='5':
                self.filtering()
            elif ch =='6':
                self.save_tasks()
            elif ch =='7':
                self.load_tasks()
            elif ch =='8':
                print("Goodbye!")
                break

            else:
                print("Invalid choice, choose from the options!")

tasks = Task_Manager(storage =CSVStorage("tasks.csv"))
tasks.menu()


                    

            