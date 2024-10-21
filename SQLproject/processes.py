import validation
import hashlib
import main
import SQLdatabase
from tkinter import messagebox as msg


def hash(inputVar):
    return hashlib.sha256(inputVar.encode('utf-8')).hexdigest()


def hash_find(win, userVar, passVar):
    if validation.validateUsername(userVar) and validation.validatePassword(passVar):
        passVar = hash(passVar)

        if SQLdatabase.searchUser(userVar, passVar):
            msg.showinfo("Logged In", "You have successfully logged in")
        else:
            msg.showinfo("User not found",  "This account doesn't exist")
            win.destroy()
            main.main()

    else:
        msg.showinfo("Invalid username or password", "Your username or password is invalid")
        win.destroy()
        main.main()

if __name__=="__main__":
    pass