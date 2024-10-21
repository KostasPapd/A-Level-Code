import sqlite3


def create_database():  # creates the table
    conn = sqlite3.connect("usersAccount.db")
    cursor = conn.cursor()
    # Create a table to store user credentials
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       username TEXT,
                       password TEXT)''')
    conn.close()



def searchUser(givenUser, givenpassword):
    conn = sqlite3.connect('usersAccount.db')
    # Select all records in a table:
    cursor = conn.execute(''' SELECT UserName, password FROM  USERS ''')
    for row in cursor:

        if row[0] == givenUser and row[1] == givenpassword:

            return True

    return False



def adduser(user, hashpass):
    create_database()
    conn = sqlite3.connect("usersAccount.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)",
                   (user, hashpass))

    conn.commit()


if __name__ == "__main__":
    # username = "Kostas"
    # password = "KostasPass123"
    # import processes
    # password = processes.hash(password)
    # print(searchUser(username, password))
    pass
