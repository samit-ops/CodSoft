import tkinter as tk
from tkinter import messagebox, Scrollbar
import math

history = []

def calculate():
    expression = entry.get()
    try:
        result = eval(expression, {"__builtins__": None}, vars(math))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
        history.append(f"{expression} = {result}")
        update_history()
    except Exception:
        messagebox.showerror("Error", "Invalid Expression")

def clear():
    entry.delete(0, tk.END)

def delete():
    current = entry.get()
    if current:
        entry.delete(len(current) - 1, tk.END)

def update_history():
    history_text.config(state=tk.NORMAL)
    history_text.delete(1.0, tk.END)
    for item in history[-100:][::-1]:
        history_text.insert(tk.END, item + "\n")
    history_text.config(state=tk.DISABLED)

def append(char):
    entry.insert(tk.END, char)

def clear_history():
    history.clear()
    update_history()
root = tk.Tk()
root.title("Calculator")
root.geometry("480x750")
root.configure(bg="#0f0f0f")
root.resizable(False, False)

accent = "#00ffcc"
btn_bg = "#1e1e1e"
btn_fg = "#ffffff"

entry = tk.Entry(root, font=("Consolas", 26), justify="right", bg="#1c1c1c", fg=accent,
                 insertbackground=accent, relief=tk.FLAT, bd=12)
entry.pack(padx=15, pady=20, fill='x')

btn_frame = tk.Frame(root, bg="#0f0f0f")
btn_frame.pack(padx=10, pady=10)

sci_buttons = [
    ['sin(', 'cos(', 'tan(', 'log('],
    ['sqrt(', 'pi', 'e', '^'],
]

standard_buttons = [
    ['7', '8', '9', '/', 'DEL'],
    ['4', '5', '6', '*', 'C'],
    ['1', '2', '3', '-', '('],
    ['0', '.', '=', '+', ')'],
]

def make_button(text, row, col, sci=False):
    def action():
        if text == 'C':
            clear()
        elif text == '=':
            calculate()
        elif text == 'DEL':
            delete()
        elif text == '^':
            append('**')
        elif text == 'pi':
            append(str(math.pi))
        elif text == 'e':
            append(str(math.e))
        else:
            append(text)

    bg = "#142828" if sci else btn_bg
    fg = accent if sci else btn_fg

    tk.Button(
        btn_frame, text=text, command=action,
        font=("Segoe UI", 14, "bold"), bg=bg, fg=fg,
        activebackground="#333333", activeforeground=accent,
        width=6, height=2, bd=0, relief="flat"
    ).grid(row=row, column=col, padx=5, pady=5)

for i, row in enumerate(sci_buttons):
    for j, text in enumerate(row):
        make_button(text, i, j, sci=True)
for i, row in enumerate(standard_buttons):
    for j, text in enumerate(row):
        make_button(text, i + 2, j)

tk.Label(root, text="History", font=("Segoe UI", 14, "bold"), bg="#0f0f0f", fg=accent).pack(pady=(10, 0))

history_frame = tk.Frame(root, bg="#0f0f0f")
history_frame.pack(padx=15, pady=(5, 0), fill='both', expand=True)

scrollbar = Scrollbar(history_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

history_text = tk.Text(
    history_frame, height=8, bg="#1a1a1a", fg=accent,
    font=("Consolas", 12), state=tk.DISABLED, relief=tk.FLAT,
    yscrollcommand=scrollbar.set
)
history_text.pack(side=tk.LEFT, fill="both", expand=True)
scrollbar.config(command=history_text.yview)

tk.Button(
    root, text="Clear History", command=clear_history,
    font=("Segoe UI", 12), bg="#1e1e1e", fg="white",
    activebackground="#2e2e2e", activeforeground=accent,
    relief="flat", bd=0, height=1
).pack(pady=10)

tk.Label(
    root,
    text="Made by SAMIT ♥",
    font=("Segoe UI", 11, "italic"),
    bg="#0f0f0f",
    fg=accent
).pack(pady=(5, 10))

root.bind("<Return>", lambda event: calculate())

root.mainloop()
