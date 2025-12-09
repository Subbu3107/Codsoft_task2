import tkinter as tk

root = tk.Tk()
root.title(" Calculator🔢➕➖✖➗")

entry = tk.Entry(root, width=35, borderwidth=5, font=('Arial', 24), justify='right', bg='lightblue', fg='black')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

expression = ""

def button_click(number):
    global expression
    expression += str(number)
    entry.delete(0, tk.END)
    entry.insert(0, expression)

def button_clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

def button_equal():
    global expression
    try:
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(0, result)
        expression = result
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        expression = ""

def create_button(text, row, col, command):
    button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=command)
    button.grid(row=row, column=col, sticky="nsew") 
    return button

# Creating buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    if text == '=':
        create_button(text, row, col, button_equal)
    elif text == 'C':
        create_button(text, row, col, button_clear)
    else:
        create_button(text, row, col, lambda t=text: button_click(t))


root.mainloop()