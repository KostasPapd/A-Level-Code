import sqlite3

def create_Students_table():
# let us create a table
    db = "./students.db"
    conn = sqlite3.connect(db)
    c = conn.cursor()
    cmd = "CREATE TABLE IF Not EXISTS students (Name TEXT, Age INT)"
    c.execute(cmd)
    data = [("Robert", 10), ("Sally", 15), ("Matthew", 7)]
    c.executemany("INSERT INTO students VALUES (?,?)", data)
    conn.commit()
    print("students table created and  3 records added")

def print_all_records():
# print all
    db = "./students.db"
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("SELECT * from students")
    allResults = c.fetchall()
    print(allResults)
    conn.close()

def show_single_record():
    db = "./students.db"
    conn = sqlite3.connect(db)
    c = conn.cursor()
    varname = input("Please Enter a name ")
    # the next two lines is the SQL statement to select the record
    sqlstring = "SELECT * from students WHERE Name='%s'" % varname
    c.executescript(sqlstring)# executes multiple SQL statements
    # now we print the result
    result = c.fetchall()
    print(result)
    conn.close()
    conn.close()

show_single_record()