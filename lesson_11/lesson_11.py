###TASK 1

import sqlite3



sql = """
    DROP TABLE IF EXISTS Roster;
    CREATE TABLE Roster(
    Name TEXT,
    Species TEXT,
    Age INT
    );
"""
populate_table = (
('Benjamin Sisko', 'Human', 40),
('Jadzia Dax', 'Trill', 300),
('Kira Nerys', 'Bajoran', 29)
)

with  sqlite3.connect("roster.db") as c:
    cursor = c.cursor()
    #1)database creation
    cursor.executescript(sql)
    #2)data inserting
    cursor.executemany("INSERT INTO Roster Values(?, ?, ?)", populate_table)
    #3) updating
    cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")
    #4) Query data
    cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
    for row in cursor.fetchall():
        print(row)
    #5) Deleting
    cursor.execute("DELETE FROM Roster WHERE Age > 100")
    #6) Adding
    #returning the ezri dax data back:
    cursor.execute("INSERT INTO Roster(Name, Species, Age) VALUES('Ezri Dax', 'Trill', 300)")
     
    cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")
    cursor.execute("UPDATE Roster SET Rank = 'Captain' WHERE Name = 'Benjamin Sisko'")
    cursor.execute("UPDATE Roster SET Rank = 'Lieutenant' WHERE Name = 'Ezri Dax'")
    cursor.execute("UPDATE Roster SET Rank = 'Major' WHERE Name = 'Kira Nerys'")

    #7) sorting by age
    cursor.execute("SELECT * FROM Roster ORDER BY Age DESC") 
    print(cursor.fetchall())

#--- TASK 2

import sqlite3

create_table = """
    DROP TABLE IF EXISTS Books;
    CREATE TABLE Books(
    Title TEXT,
    Author TEXT,
    Year_Published INT,
    Genre TEXT
    );
"""

data = (
    ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
    ('1984', 'George Orwell', 1949, 'Dystopian'),
    ('The Great  Gatsby', 'F.Scott Fitzgerald', 1925, 'Classic')
)

with sqlite3.connect("library.db") as c:
    cursor = c.cursor()
    cursor.executescript(create_table)
    cursor.executemany("INSERT INTO Books Values(?, ?, ?, ?)", data)

    cursor.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")

    cursor.execute("SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")

    cursor.execute("INSERT INTO Books(Title, Author, Year_Published, Genre) VALUES('The Great Gatsby', 'F.Scott Fitzgerald', 1925, 'Classic')")
    cursor.execute("ALTER TABLE Books ADD COLUMN Rating INT")
    cursor.execute("UPDATE Books SET Rating = 4.8 WHERE Title = 'To Kill a Mockingbird'")
    cursor.execute("UPDATE Books SET Rating = 4.7 WHERE Title = '1984'")
    cursor.execute("UPDATE Books SET Rating = 4.5 WHERE Title = 'The Great Gatsby'")

    cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
    print(cursor.fetchall())