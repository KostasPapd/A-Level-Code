from tkinter import *
from processes import *


def getVal(win, passBox, userBox):
    username = userBox.get().strip()
    password = passBox.get().strip()

    hash_find(win, username, password)


def clear(passw, user):
    passw.delete(0, 'end')
    user.delete(0, 'end')
    user.focus()


def createMenu():
    win = Tk()

    wWidth = 500
    wHeight = 300
    xCord = int((win.winfo_screenwidth() / 2) - (wWidth / 2))
    yCord = int((win.winfo_screenheight() / 2) - (wHeight / 2))
    win.geometry(f"{wWidth}x{wHeight}+{xCord}+{yCord}")

    win.title("Log In")

    usernameLabel = Label(win, text="Username:")
    usernameLabel.config(font=("Arial", 16))
    usernameLabel.place(relx=0.05, rely=0.18, relwidth=0.3, relheight=0.1)

    userBox = Entry(win)
    userBox.place(relx=0.33, rely=0.2, relheight=0.07, relwidth=0.5)

    passLabel = Label(win, text="Password:")
    passLabel.config(font=("Arial", 16))
    passLabel.place(relx=0.04, rely=0.4, relwidth=0.3, relheight=0.1)

    passBox = Entry(win, show="*")
    passBox.place(relx=0.33, rely=0.42, relheight=0.07, relwidth=0.5)

    logButton = Button(win, text="Log In", command=lambda: getVal(win, passBox, userBox))
    logButton.config(font=("Arial", 16))
    logButton.place(relx=0.7, rely=0.7, relheight=0.15, relwidth=0.2)

    clearButton = Button(win, text="Clear", command=lambda: clear(passBox, userBox))
    clearButton.config(font=("Arial", 16))
    clearButton.place(relx=0.4, rely=0.7, relheight=0.15, relwidth=0.2)

    exitButton = Button(win, text="Exit", command=quit)
    exitButton.config(font=("Arial", 16))
    exitButton.place(relx=0.1, rely=0.7, relheight=0.15, relwidth=0.2)

    userBox.focus()
    win.resizable(False, False)
    win.mainloop()


if __name__ == "__main__":
    createMenu()
