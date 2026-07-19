class Vector:
    def __init__(self, *args):
        self.components = args

    def __str__(self):
        return(f"Vector({", " .join(str(c) for c in self.components)}")

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("The number of dimensions must be equal")
        new_components = [a+b for a,b in zip((self.components), other.components)]
        return new_components
    def __sub__ (self, other):
        if len(self.components) != len(other.components):
            raise ValueError("The number of dimensions must be equal")
        new_components = [a - b for a,b in zip(self.components, other.components)]
        return new_components

    def __mul__(self,other):
        if len(self.components) != len(other.components):
            raise ValueError("The number of dimensions must be equal")
        return sum(a*b for a,b in zip(self.components, other.components))
        

    def __rmul__(self, scalar):
        new_components = [scalar*c for c in self.components]
        return new_components
    

    def magnitude(self):
        import math
        magn = math.sqrt(sum(c**2 for c in self.components))
        return magn

    def normalize(self):
        mag = self.magnitude()
        norm = [round(c / mag, 3) for c in self.components]
        return Vector(*norm)
    
v1 = Vector(1,2,3)
print(v1.components)

v2 = Vector(4,5,6)

v3 = v1+v2
print(v3)

v4 = v2 - v1
print(v4)

dot_product = v1*v2
print(dot_product)

v5 = 3*v1
print(v5)

print(v1.magnitude())

v_unit = v1.normalize()
print(v_unit)




###TASK 2

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"
#bumba = Employee(1001, 'Bumba', 'Da Boss', 45600)
#print(bumba.employee_id)

class EmployeeManager:
    def __init__(self, filename = 'employees.txt'):
        self.filename = filename
        self.employees = {}
        self.load_employees() 

    def add_employee(self):
        employee_id = input("Enter ID of an Employee: ")
        name = input("Enter employee name: ")
        position = input("Enter employee's postion: ")
        salary = input("Enter Employee's salary: ")

        self.employees[employee_id] = Employee(employee_id, name, position, salary)
        self.save_employees()
        print("Employee successfully added!")
        
    def load_employees(self):
        try:
            with open('employees.txt', 'r') as r:
                for line in r:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(', ')
                    employee_id, name, position, salary = parts
                    self.employees[employee_id] = Employee(employee_id, name, position, salary)
        except FileNotFoundError:
            print("Such file does not exist")
                    

    def save_employees(self):
        with open(self.filename, 'w') as f:
            for emp in self.employees.values():
                f.write(f"{emp.employee_id}, {emp.name}, {emp.position}, {emp.salary} \n")
    
    def view_all(self):
        for n in self.employees.values():
            print(n)
    
    def search(self):
        ask = input("Enter employee's ID: ")
        if ask in self.employees:
            idd = self.employees[ask]
            print(f"ID : {idd.employee_id},\n Name : {idd.name},\n Position: {idd.position},\n Salary: {idd.salary}")

    def update(self):
        ask = input("Enter employee's ID to update: ")
        if ask in self.employees:
            idd = self.employees[ask]
            idd.name = input("Enter a new name: ")
            idd.position = input("Enter a new position: ")
            idd.salary = input("Enter a new salary: ")
            self.save_employees()
            print("Employee successfully updated!")
        else:
            print("No such employee")

    def delete_emp(self):
        ask = input("Enter employee's ID to delete: ")
        if ask in self.employees:
            del self.employees[ask]
            self.save_employees()
            print("Record successfully deleted")
        else:
            print("No such employee")
    def menu(self):
        print("Welcome to the Employee Manager menu!")
        while True:
            print(""" 1) Add new employee record
2) View All employee records
3)Search for an employee by an Employee ID
4)Update an employee's information
5)Delete an employee's record
6)Exit
                    """)
            choice = input("Enter a number from a menu : ")
            if choice == "1":
                self.add_employee()
            elif choice =="2":
                self.view_all()
            elif choice =="3":
                self.search()
            elif choice =="4":
                self.update()
            elif choice =="5":
                self.delete_emp()
            elif choice =="6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, choose a number from the options!")
                      
manager = EmployeeManager()
manager.menu()



###TASK 3


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