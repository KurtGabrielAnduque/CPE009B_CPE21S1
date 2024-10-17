from tkinter import *
from Registration import Register


if __name__ == '__main__':
    GUI = Tk()
    GUI.geometry('800x500')
    GUI.title("ACC SECURITY")
    mywin = Register(GUI)

    GUI.mainloop()