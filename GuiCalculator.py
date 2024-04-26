import tkinter as tk

def calculate_result():
   try:
       num1 = float(entry_num1.get())
       num2 = float(entry_num2.get())
       operator = operator_var.get()

       if operator == "+":
           result = num1 + num2
       elif operator == "-":
           result = num1 - num2
       elif operator == "*":
           result = num1 * num2
       elif operator == "/":
           result = num1 / num2

       result_label.config(text=f"Result: {result}")
   except ValueError:
       result_label.config(text="Error: Invalid input!")

root = tk.Tk()
root.title("Simple Calculator")

entry_num1 = tk.Entry(root)
entry_num1.pack()

operator_var = tk.StringVar()
operator_choices = ["+", "-", "*", "/"]
operator_var.set("+")  # Set the initial operator to '+'
operator_menu = tk.OptionMenu(root, operator_var, *operator_choices)
operator_menu.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_result)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()