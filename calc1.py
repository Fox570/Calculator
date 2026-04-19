import tkinter as tk

BG = "#202020"
BTN = "#2a2a2a"
BTN_LIGHT = "#3a3a3a"
ACCENT = "#4cc2ff"
TEXT = "#ffffff"

def add(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("320x480")
root.configure(bg=BG)
root.resizable(True, True)

frame = tk.Frame(root, bg=BG)
frame.pack(expand=True, fill="both")

# дисплей
entry = tk.Entry(
    frame,
    font=("Segoe UI", 28),
    bg=BG,
    fg=TEXT,
    borderwidth=0,
    justify="right",
    insertbackground="white"
)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=(20,10))

# кнопки
buttons = [
    ("C", clear, BTN_LIGHT),
    ("(", lambda: add("("), BTN),
    (")", lambda: add(")"), BTN),
    ("/", lambda: add("/"), BTN_LIGHT),

    ("7", lambda: add("7"), BTN),
    ("8", lambda: add("8"), BTN),
    ("9", lambda: add("9"), BTN),
    ("*", lambda: add("*"), BTN_LIGHT),

    ("4", lambda: add("4"), BTN),
    ("5", lambda: add("5"), BTN),
    ("6", lambda: add("6"), BTN),
    ("-", lambda: add("-"), BTN_LIGHT),

    ("1", lambda: add("1"), BTN),
    ("2", lambda: add("2"), BTN),
    ("3", lambda: add("3"), BTN),
    ("+", lambda: add("+"), BTN_LIGHT),

    ("0", lambda: add("0"), BTN),
    (".", lambda: add("."), BTN),
    ("=", calculate, ACCENT),
]

row = 1
col = 0

for (text, cmd, color) in buttons:
    b = tk.Button(
        frame,
        text=text,
        command=cmd,
        bg=color,
        fg=TEXT,
        font=("Segoe UI", 14),
        borderwidth=0,
        activebackground="#505050",
        activeforeground="white"
    )
    b.grid(row=row, column=col, sticky="nsew", padx=4, pady=4)

    col += 1
    if col > 3:
        col = 0
        row += 1

# адаптивная сетка
for i in range(row + 1):
    frame.rowconfigure(i, weight=1)

for j in range(4):
    frame.columnconfigure(j, weight=1)

root.mainloop()