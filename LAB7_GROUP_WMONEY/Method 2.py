from tkinter import *


def findLargest():
    L = []
    L.append(eval(number1.get()))
    L.append(eval(number2.get()))
    L.append(eval(number3.get()))
    LARGEST.set(max(L))


GUI = Tk()

GUI.title("Find the largest number")
GUI.geometry("400x330")

number1 = StringVar()
number2 = StringVar()
number3 = StringVar()
LARGEST = StringVar()

mainlabel = Label(GUI, text = "The Program that Finds the Largest Number")
mainlabel.grid(row = 0, column = 1, columnspan = 2 , sticky = EW)

label1 = Label(GUI, text = "Enter the first number: ")
label1.grid(row = 1,column = 0, sticky = W)
Entry1 = Entry(GUI,bd = 3, textvariable= number1 )
Entry1.grid(row = 1, column = 1)

Label2 = Label(GUI, text = "Enter the second number: ")
Label2.grid(row = 2, column = 0)
Entry2 = Entry(GUI, bd = 3, textvariable= number2)
Entry2.grid(row = 2, column = 1)

Label3 = Label(GUI, text = "Enter the third number: ")
Label3.grid(row = 3, column = 0)
Entry3 = Entry(GUI, bd=3 ,textvariable= number3)
Entry3.grid(row = 3 ,column = 1)


Button1 = Button(GUI, text = "Search", command= findLargest)
Button1.grid(row = 4, column = 1)


Label4 = Label(GUI, text = "The largest Number is: ")
Label4.grid(row=5,column = 0)

Entry4 = Entry(GUI,bd = 3,state = "readonly", textvariable= LARGEST)
Entry4.grid(row= 5, column = 1)

GUI.mainloop()