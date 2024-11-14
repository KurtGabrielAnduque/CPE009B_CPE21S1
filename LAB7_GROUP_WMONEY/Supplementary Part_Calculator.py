import tkinter as tk
from tkinter import messagebox
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("440x340")
        self.history_file = "calculator_history.txt"


        self.initUI()

    def initUI(self):

        self.textLine = tk.Entry(self, font=('Arial', 20), bd=10, relief='sunken', justify='right')
        self.textLine.grid(row=0, column=0, columnspan=5, sticky="nsew")

        # Button labels
        names = [
            '7', '8', '9', '/', 'Clear',
            '4', '5', '6', '*', 'sin',
            '1', '2', '3', '-', 'cos',
            '0', '.', '=', '+', 'exp'
        ]

        # Create buttons and place them in a grid
        for i, name in enumerate(names):
            button = tk.Button(self, text=name, font=('Arial', 14),bg = 'light goldenrod', width=6, height=2, command=lambda name= name: self.on_button_clicked(name))
            row, col = divmod(i, 5)
            button.grid(row=row+1, column=col, padx=5, pady=5)


        self.load_menu()

    def load_menu(self):
        menu_bar = tk.Menu(self)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Clear History", command=self.clear_history)
        file_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        self.config(menu=menu_bar)

    def on_button_clicked(self, button_text):
        if button_text == 'Clear':
            self.textLine.delete(0, tk.END)
        elif button_text == '=':
            self.calculate_result()
        elif button_text in ['sin', 'cos', 'exp']:
            self.perform_trig_or_exp(button_text)
        else:
            current_text = self.textLine.get()
            new_text = current_text + button_text
            self.textLine.delete(0, tk.END)
            self.textLine.insert(tk.END, new_text)

    def calculate_result(self):
        expression = self.textLine.get()
        try:
            result = eval(expression)
            self.textLine.delete(0, tk.END)
            self.textLine.insert(tk.END, str(result))
            self.save_to_history(f"{expression} = {result}")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Expression: {str(e)}")

    def perform_trig_or_exp(self, operation):
        try:
            value = float(self.textLine.get())
            if operation == 'sin':
                result = math.sin(math.radians(value))
            elif operation == 'cos':
                result = math.cos(math.radians(value))
            elif operation == 'exp':
                result = math.exp(value)
            self.textLine.delete(0, tk.END)
            self.textLine.insert(tk.END, str(result))
            self.save_to_history(f"{operation}({value}) = {result}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_to_history(self, entry):
        with open(self.history_file, 'a') as f:
            f.write(entry + '\n')

    def clear_history(self):
        try:
            with open(self.history_file, 'w') as f:
                f.truncate()
            messagebox.showinfo("Success", "History cleared.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == '__main__':
    app = Calculator()
    app.mainloop()
