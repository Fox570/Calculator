import tkinter as tk
from tkinter import messagebox
from keyboard import add_hotkey

# functions
def make_digit_btn(digit):
    return tk.Button(win, text=digit, bd=0, font=("Helvetica", 15), bg="#e67e22", command=lambda: add_digit(digit),\
        activebackground="#E09049")

def make_operation_btn(operation):
    return tk.Button(win, text=operation, bd=0, font=("Helvetica", 15), bg="#e74c3c", command=lambda: add_operation(operation),\
        activebackground="#E66053")

def make_calc_btn(operation):
    return tk.Button(win, text=operation, bd=0, font=("Helvetica", 15), bg="#e74c3c", command=calculate,\
        activebackground="#E66053")

def make_clear_btn(operation):
    return tk.Button(win, text=operation, bd=0, font=("Helvetica", 15), bg="#e74c3c", command=clear,\
        activebackground="#E66053")

def add_digit(digit):
    value = calc.get()
    if value[0] == "0" and len(value) == 1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value + digit)
    
def add_operation(operation):
    value = calc.get()
    if value and value[-1] in "+-/*":
        value = value[:-1]
    elif "+" or "-" or "*" or "/" in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)
    
def calculate():
    value = calc.get()
    if value[-1] in "+-*/":
        value=value+value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except ZeroDivisionError:
        calc.insert(0, "error")
    except (NameError, SyntaxError):
        messagebox.showinfo("Внимание", "Нужно вводить только числа!")
        clear()
        
def clear():
    calc.delete(0, tk.END)
    calc.insert(0, "0")
    
def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in "+-*/":
        add_operation(event.char)
    elif event.char == '\r':
        calculate()
        
add_hotkey('c', clear)


win = tk.Tk()

# window settings
win.title("Calculator")
icon = tk.PhotoImage(file="calculator.png")
win.iconphoto(False, icon)

win.bind("<Key>", press_key)

w = 300
h = 328

win.geometry(f"{w}x{h}+1000+150")
win["bg"] = "black"
win.resizable(False, False)

# Vidgets
calc = tk.Entry(win, justify=tk.RIGHT, font=("Helvetica", 33), width=10, bg="black", fg="white", bd=0)
calc.insert(0, "0")
calc.grid(row=0, column=0, columnspan=4, sticky="we", pady=2)

make_digit_btn("7").grid(row=1, column=0, sticky="wens", padx=1, pady=1)
make_digit_btn("8").grid(row=1, column=1, sticky="wens", padx=1, pady=1)
make_digit_btn("9").grid(row=1, column=2, sticky="wens", padx=1, pady=1)
make_digit_btn("4").grid(row=2, column=0, sticky="wens", padx=1, pady=1)
make_digit_btn("5").grid(row=2, column=1, sticky="wens", padx=1, pady=1)
make_digit_btn("6").grid(row=2, column=2, sticky="wens", padx=1, pady=1)
make_digit_btn("1").grid(row=3, column=0, sticky="wens", padx=1, pady=1)
make_digit_btn("2").grid(row=3, column=1, sticky="wens", padx=1, pady=1)
make_digit_btn("3").grid(row=3, column=2, sticky="wens", padx=1, pady=1)
make_digit_btn("0").grid(row=4, column=0, sticky="wens", padx=1, pady=1)

make_operation_btn("+").grid(row=4, column=3, sticky="wens", padx=1, pady=1)
make_operation_btn("-").grid(row=3, column=3, sticky="wens", padx=1, pady=1)
make_operation_btn("/").grid(row=2, column=3, sticky="wens", padx=1, pady=1)
make_operation_btn("*").grid(row=1, column=3, sticky="wens", padx=1, pady=1)
make_calc_btn("=").grid(row=4, column=2, sticky="wens", padx=1, pady=1)
make_clear_btn("C").grid(row=4, column=1, sticky="wens", padx=1, pady=1)


win.grid_columnconfigure(0, minsize=75)
win.grid_columnconfigure(1, minsize=75)
win.grid_columnconfigure(2, minsize=75)
win.grid_columnconfigure(3, minsize=75)

win.grid_rowconfigure(1, minsize=68)
win.grid_rowconfigure(2, minsize=68)
win.grid_rowconfigure(3, minsize=68)
win.grid_rowconfigure(4, minsize=68)

win.mainloop()