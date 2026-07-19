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

