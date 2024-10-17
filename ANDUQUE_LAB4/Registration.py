from tkinter import *

class Register:


    def Submit(self):
        name1 = self.Entry1.get()
        name2 = self.Entry2.get()
        name3 = self.Entry3.get()
        name4 = self.Entry4.get()
        name5 = self.Entry5.get()
        name6 = self.Entry6.get()


        if name1 == "" or name2 == "" or name3 == "" or name4 == "" or name5 == "" or name6 == "":
            self.notif.config(fg="red", text="All fields must fill!!")


        else:
            self.notif.config(fg="green", text="ACCOUNT IS SUCCESSFULLY REGISTERED :>")
            self.clear()


    def clear(self):
        self.Entry1.delete(0, END)
        self.Entry2.delete(0, END)
        self.Entry3.delete(0, END)
        self.Entry4.delete(0, END)
        self.Entry5.delete(0, END)
        self.Entry6.delete(0, END)


    def __init__(self, GUI):
        self.GUI = GUI

        #LABEL INSIDE REGISTER WINDWOW
        self.Label1 = Label(self.GUI, text = "Please complete all required fields", font = ('Arial', 20))
        self.Label1.pack(padx = 10, pady = 10)

        self.Label2 = Label(self.GUI, text = "First Name : ", font = ('Arial', 15))
        self.Label2.place(x = 50, y = 100, height = 50, width = 200 )

        self.Label3 = Label(self.GUI, text="Last Name : ", font=('Arial', 15))
        self.Label3.place(x=50, y=150, height=50, width=200)

        self.Label4 = Label(self.GUI, text="User Name : ", font=('Arial', 15))
        self.Label4.place(x=50, y=200, height=50, width=200)

        self.Label5 = Label(self.GUI, text="Password : ", font=('Arial', 15))
        self.Label5.place(x=50, y=250, height=50, width=200)

        self.Label6 = Label(self.GUI, text = "E-mail: ", font= ('Arial',15))
        self.Label6.place(x=50, y = 300, height = 50, width = 200)

        self.Label7 = Label(self.GUI, text = "Contact No. : ", font = ('Arial', 15))
        self.Label7.place(x= 50, y = 350, height = 50, width = 200)





        #Entry for every fields

        self.Entry1 = Entry(self.GUI, font = ('Arial',15),bd = 2)
        self.Entry1.place(x = 210, y = 100, height = 40, width = 400)

        self.Entry2 = Entry(self.GUI,  font = ('Arial',15),bd = 2)
        self.Entry2.place(x=210, y=150, height=40, width=400)


        self.Entry3 = Entry(self.GUI, font = ('Arial', 15),bd = 2)
        self.Entry3.place(x=210, y=200, height = 40, width=400)

        self.Entry4 = Entry(self.GUI, show="*",bd = 2)
        self.Entry4.place(x=210, y=250, height=40, width=400)

        self.Entry5 = Entry(self.GUI, font=('Arial', 15),bd = 2)
        self.Entry5.place(x=210, y=300, height=40, width=400)

        self.Entry6 = Entry(self.GUI, font=('Arial', 15),bd = 2)
        self.Entry6.place(x=210, y=350, height=40, width=400)


        self.Button1 = Button(self.GUI, text="Submit", font=('Arial',15),command= self.Submit)
        self.Button1.place(x=300, y= 420, height = 40 , width = 100)

        self.Button2 = Button(self.GUI, text = "Clear", font = ('Arial',15),command= self.clear)
        self.Button2.place(x= 400, y= 420, height = 40, width = 100)

        self.notif = Label(self.GUI, font=('Arial', 15))
        self.notif.pack(padx=15, pady=10)