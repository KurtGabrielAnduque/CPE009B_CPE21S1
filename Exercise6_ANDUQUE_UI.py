from tkinter import *

class MyWindow:
    def Close(self):
        window.destroy


    def Add(self):
        self.Elbl3.delete(0,'end')
        num1 = int(self.Elbl1.get())
        num2 = int(self.Elbl2.get())
        result = num1 +num2
        self.Elbl3.insert(END,str(result))


    def Sub(self):
        self.Elbl3.delete(0,'end')
        num1 = int(self.Elbl1.get())
        num2 = int(self.Elbl2.get())
        result = num1 - num2
        self.Elbl3.insert(END,str(result))


    def Mul(self):
        self.Elbl3.delete(0,'end')
        num1 = int(self.Elbl1.get())
        num2 = int(self.Elbl2.get())
        result = num1 * num2
        self.Elbl3.insert(END,str(result))

    def Div(self):
        self.Elbl3.delete(0,'end')
        num1 = int(self.Elbl1.get())
        num2 = int(self.Elbl2.get())
        if(num2 != 0 ):
            result = num1 / num2
            self.Elbl3.insert(END, str(result))
        else:
            self.Elbl3.delete(0, 'end')
            self.Elbl3.insert(END,"ERROR")




    def clear(self):
        self.Elbl1.delete(0,END)
        self.Elbl2.delete(0,END)
        self.Elbl3.delete(0,END)

    def __init__(self, window):


        self.mainlabel = Label(window,text = "---SIMPLE CALCULATOR---", font =('Arial',30))
        self.mainlabel.pack(padx = 50 ,pady = 50)


        self.lbl1 = Label(window, text="Number1: ", font=('Arial', 20))
        self.lbl1.place(x=200, y = 200)

        self.lbl2 = Label(window, text = "Number2:",font =('Arial',20))
        self.lbl2.place(x=200, y = 250)

        self.lbl3 = Label(window, text="Result", font=('Arial', 20))
        self.lbl3.place(x=200, y=300)

        self.Elbl1 = Entry(window, font = ('Arial',15))
        self.Elbl1.place(x = 350 , y = 200, width = 200, height = 40)

        self.Elbl2 = Entry(window, font=('Arial', 15))
        self.Elbl2.place(x=350, y=250, width=200, height=40)

        self.Elbl3 = Entry(window, font=('Arial', 15))
        self.Elbl3.place(x=350, y=300, width=200, height=40)

        self.sub_button = Button(window, text="Subtract", font=('Aria', 30), command=self.Sub)
        self.sub_button.place(x=400, y=400, width=200, height=50)

        self.sum_button = Button(window, text = "Add", font =('Aria',30), command= self.Add)
        self.sum_button.place(x= 150, y = 400,width = 200, height = 50)

        self.mul_button = Button(window,text="Multiply",font=('Arial',30), command= self.Mul)
        self.mul_button.place(x= 150, y = 500, width = 200, height = 50)

        self.div_button = Button(window,text="Divide", font=('Arial',30),command= self.Div)
        self.div_button.place(x = 400 , y = 500, width = 200, height = 50)

        self.exit_button = Button(window, text="Exit",font=('Arial',30), command=window.destroy)
        self.exit_button.place(x = 300, y = 600, width = 200, height = 50)

        self.clear_but = Button(window,text =" Clear", font=('Arial',15), command= self.clear)
        self.clear_but.place(x= 600, y = 200, width = 80, height = 100)





window = Tk()
window.geometry("800x800")
window.title('CALCULATOR')
mywin = MyWindow(window)
window.mainloop()
