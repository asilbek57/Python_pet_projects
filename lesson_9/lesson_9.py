###TASK 1

class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author, is_borrowed = False):
        if not isinstance(title, str):
                    raise ValueError ('Title must be a string!')
        self.title = title
        if not isinstance(author, str):
                    raise ValueError ('Author must be a string!')
        self.author = author

        self.is_borrowed = is_borrowed
    
    def __str__(self):
        return (f"{self.title},{self.author},{self.is_borrowed}")

class Member:
    def __init__(self, name, borrowed_books = None):
        if not isinstance(name, str):
            raise ValueError ('Name must be a string!')
        self.name = name
        self.borrowed_books = borrowed_books if borrowed_books is not None else []

    def __str__(self):
        return(f"{self.name},{self.borrowed_books}")

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, title, author, is_borrowed=False):
        new_book = Book(title, author, is_borrowed)
        self.books[title] = new_book

    def add_member(self,name, borrowed_books=None):
        new_member = Member(name, borrowed_books)
        self.members[name] = new_member

    def borrow(self, book_name, member_name):
        if member_name not in self.members:
            print("No such member in our library!")
        elif book_name not in self.books:
            raise BookNotFoundException ("Unfortunetaly, there is no such book yet.")

        member = self.members[member_name]
        book = self.books[book_name]
        if book.is_borrowed == True:
            raise BookAlreadyBorrowedException ('This book is already borrowed!')
             
        else:

            
            if len(member.borrowed_books) >= 3:
                raise MemberLimitExceededException ('Limit to borrow books has been reached!')
            else:
                member.borrowed_books.append(book_name)

            book.is_borrowed = True
            print(f"{member.name} borrowed book named {book.title}. Number of his borrowed books : {len(member.borrowed_books)}")



    def returning(self, book_name, member_name):
        if member_name not in self.members:
            print("No such member in our library!")
        elif book_name not in self.books:
            raise BookNotFoundException ("Unfortunetaly, there is no such book yet.")
        else:
            member = self.members[member_name]
            member.borrowed_books.remove(book_name)
            book = self.books[book_name]
            book.is_borrowed = False
            print(f"{book.title} has been returned by {member.name}. Number of borrowed books: {len(member.borrowed_books)}")
         
john = Library()
john.add_book('1984','George Orwell')
john.add_book('Animal Farm','George Orwell')
john.add_book('Harry Potter : Philosophical Stone','J.K.Rowling')
john.add_book('Metamorphosis','Kafka')
john.add_member('Harry')
john.add_member('Max')
john.borrow('1984', 'Harry')
john.borrow('Animal Farm', 'Max')
john.returning('1984', 'Harry')



###TASK 2

class Grades:
    def __init__(self):
        self.columns = []
        self.data = []

    def storing(self):
        try:
            with open('grades.csv', 'r') as file:
                import csv
                reader = csv.reader(file)
                self.columns = next(reader)
                for row in reader:
                    self.data.append(row)                            
        except FileNotFoundError:
            print("No such file!")
        print(self.columns)
        print(self.data)

    def avg_grade(self):
        grades_dict = {}
        for row in self.data:
            name, subject, grade = row
            grade = float(grade)

            if subject not in grades_dict:
                grades_dict[subject] = []
            grades_dict[subject].append(grade)

        averages = {}
        for subject, grade_list in grades_dict.items():
            averages[subject] = sum(grade_list)/len(grade_list)

        with open('average_grades.csv', 'w', newline = '') as f:
            import csv
            writer = csv.writer(f)
            writer.writerow(['Subject','Average Grade'])
            for subject, avg in averages.items():
                writer.writerow([subject,avg])


sub = Grades()
sub.storing()
sub.avg_grade()



###TASK 3
class Json:
    def __init__(self):
        self.tasks = []

    def load(self):
        import json
        with open('tasks.json', 'r') as f:
            self.tasks = json.load(f)
            for data in self.tasks:
                print(f"ID: {data['id']}, Task: {data['task']}, Completed Staus: {data['completed']}, Priority: {data['priority']}")
        
            

    def save(self):
        import json
        with open('tasks.json', 'w') as f:
            json.dump(self.tasks, f, indent = 4)

    def change(self):
        ask = int(input('Enter Task ID: '))
        found = False
        
        for task in self.tasks:

            if task['id'] == ask:
                new_status = input("Enter new status: ")
                if new_status.lower() == 'true':
                    task['completed'] = True
                elif new_status.lower() == 'false':
                    task['completed'] = False
                found = True             
                break
            if not found:
                print("No such task")
        self.save()


    def count(self):
        total_num = len(self.tasks)
        print(f"Total number of tasks: {total_num}")

        com_tasks = 0
        for task in self.tasks:
            if task['completed'] == True:
                com_tasks += 1
        print(com_tasks)

        uncom_tasks = 0
        for task in self.tasks:
            if task['completed'] == False:
                uncom_tasks += 1
        print(uncom_tasks)

        average_priority = []
        for task in self.tasks:
            average_priority.append(task['priority'])
        average = (sum(average_priority)/len(average_priority))
        print(average)

    def json_to_csv(self):
        import json
        import csv

        with open("tasks.json", "r") as f:
            data = json.load(f)


        with open("tasks.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Task", "Completed", "Priority"]) 

            for task in data:
                writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])

check = Json()
check.load()
check.change()
check.count()