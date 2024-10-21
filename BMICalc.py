from tkinter import *
from tkinter import messagebox

def empty(w, h):
    w.delete(0, 'end')
    h.delete(0, 'end')
    w.focus()

def calcBMI(f, w, h):
    h = float(h.get())
    w = float(w.get())
    bmi = w/(h*h)
    bmi = round(bmi, 2)
    result = "Your BMI is " + str(bmi)
    messagebox.showinfo(title="BMI value", message=result)
    msgBox = messagebox.askquestion(title="Retry?", message="Do you want to retry?")
    if msgBox == "yes":
        f.destroy()
        CreateGUI()
    else:
        quit()

def CreateGUI():
    form = Tk()
    form.title("Welcome to BMI calculator")
    form.geometry("500x220")
    welcomeLabel = Label(form, text=" Welcome to my BMI calculator")
    welcomeLabel.config(font=("Courier", 14))
    welcomeLabel.grid(row=0, column=0, columnspan=3, sticky="W", padx=10, pady=10)

    weightLabel = Label(form, text="Weight in Kg")
    weightLabel.config(font=("Arial", 10))
    weightLabel.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    heightLabel = Label(form, text="Height in Meters")
    heightLabel.config(font=("Arial", 10))
    heightLabel.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    helpLabel= Label(form, text="Enter height(m)and weight(Kg)")
    helpLabel.config(font=("Arial", 8))
    helpLabel.grid(row=1, rowspan=2, column=2, padx=10, pady=10)

    weightEntry = Entry(form, width=30)
    weightEntry.grid(row=1, column=1, padx=10, pady=10, sticky="E")

    heightEntry = Entry(form, width=30)
    heightEntry.grid(row=2, column=1, padx=10, pady=10, sticky="E")

    exitButton = Button(form, text="Exit", width=12, command=quit)
    exitButton.grid(row=3, column=0, padx=10, pady=10, sticky="E")

    clearButton = Button(form, text="Clear", width=12, command=lambda: empty(weightEntry, heightEntry))
    clearButton.grid(row=3, column=1, padx=10, pady=10)

    calcButton = Button(form, text="Calculate", width=12, command=lambda: calcBMI(form, weightEntry, heightEntry))
    calcButton.grid(row=3, column=2, padx=10, pady=10, sticky="W")

    weightEntry.focus()
    form.mainloop()

CreateGUI()
