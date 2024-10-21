from tkinter import *
from tkinter import messagebox
import codecs

def cipher(f, m):
    m = str(m.get())
    coddedMess = codecs.encode(m, 'rot_13')
    file = open('encoded.txt', "a")
    file.write(coddedMess)
    file.write("\n")
    file.close()
    result = "Message: " + coddedMess
    f.destroy()
    messagebox.showinfo(title="Encoded message", message=result)
    msgBox = messagebox.askquestion(title="Retry?", message="Do you want to retry?")
    if msgBox == "yes":
        create1()
    else:
        quit()

def create(b):
    b.destroy()
    form = Tk()
    form.title("ROT13 cipher")
    form.geometry("550x150")

    welcomeLabel = Label(form, text=" Welcome to the ROT13 cipher encryption")
    welcomeLabel.config(font=("Courier", 14))
    welcomeLabel.grid(row=0, column=0, columnspan=3, sticky="W", padx=10, pady=10)

    messLabel = Label(form, text="Message:")
    messLabel.config(font=("Arial", 10))
    messLabel.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    messEntry = Entry(form, width=65)
    messEntry.grid(row=1, column=1, padx=10, pady=10, sticky="E")

    entryButton = Button(form, text="Execute cipher", width=13, command=lambda: cipher(form, messEntry))
    entryButton.grid(row=3, column=0, padx=10, pady=10, sticky="W")

    exitButton = Button(form, text="Exit", width=13, command=quit)
    exitButton.grid(row=3, column=1, padx=10, pady=10, sticky="W")

    messEntry.focus()
    form.mainloop()

def create1():
    box = Tk()
    box.title("ROT13 cipher")
    box.geometry("500x100")
    welcomeLabel = Label(box, text="Choose encrypt or decrypt message:")
    welcomeLabel.config(font=("Courier", 14))
    welcomeLabel.grid(row=0, column=0, columnspan=3, sticky="W", padx=10, pady=10)

    dButton = Button(box, text="Decrypt message", width=13, command=lambda: create(box))
    dButton.grid(row=6, column=1, padx=10, pady=10, sticky="W")

    eButton = Button(box, text="Encrypt message", width=13, command=lambda: create(box))
    eButton.grid(row=6, column=2, padx=10, pady=10, sticky="E")

    box.mainloop()

create1()
