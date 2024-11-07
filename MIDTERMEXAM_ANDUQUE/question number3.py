import tkinter as tk

class Register(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Midterm in OOP")
        self.geometry("500x250")

        self.label = tk.Label(self, text="Enter your fullname:", fg="red")
        self.label.place(x=10, y=60, height = 20, width = 150)

        self.name_input = tk.Entry(self,border= 4, font=('Arial',15) )
        self.name_input.place(x=260, y=60, width = 200, height = 30)

        self.button = tk.Button(self, text="Click to display your Fullname", command=self.display_name, fg="red")
        self.button.place(x=30, y=120, height = 30, width = 170)

        self.output = tk.Entry(self, state='readonly', border= 4,font=('Arial',15))
        self.output.place(x=260, y=120, width = 200, height = 30)

    def display_name(self):
        name = self.name_input.get()
        self.output.config(state='normal')
        self.output.delete(0, tk.END)
        self.output.insert(0, name)
        self.output.config(state='readonly')

if __name__ == "__main__":
    app = Register()
    app.mainloop()