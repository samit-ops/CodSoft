import tkinter as tk
from tkinter import ttk, messagebox

history = []

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
        history.append(f"{expression} = {result}")
        update_history()
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")

def clear():
    entry.delete(0, tk.END)

def delete():
    entry.delete(len(entry.get()) - 1)

def update_history():
    history_text.config(state=tk.NORMAL)
    history_text.delete(1.0, tk.END)
    for item in history[-10:][::-1]:  
        history_text.insert(tk.END, item + "\n")
    history_text.config(state=tk.DISABLED)


def append(char):
    entry.insert(tk.END, char)


root = tk.Tk()
root.title("Smart Calculator")
root.geometry("400x600")
root.config(bg="#121212")
root.resizable(False, False)


style = ttk.Style()
style.theme_use("clam")

entry = ttk.Entry(root, font=("Segoe UI", 22), justify="right")
entry.pack(padx=10, pady=20, fill='x')


btn_frame = tk.Frame(root, bg="#121212")
btn_frame.pack(padx=10, pady=10)


buttons = [
    ['7', '8', '9', '/', 'DEL'],
    ['4', '5', '6', '*', 'C'],
    ['1', '2', '3', '-', '('],
    ['0', '.', '=', '+', ')'],
]

for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        action = lambda x=btn_text: append(x) if x not in ['C', '=', 'DEL'] else (
            clear() if x == 'C' else (calculate() if x == '=' else delete())
        )
        tk.Button(
            btn_frame, text=btn_text, font=("Segoe UI", 18),
            bg="#1f1f1f", fg="white", width=4, height=2,
            bd=0, relief="flat", highlightthickness=0,
            command=action
        ).grid(row=i, column=j, padx=5, pady=5)


tk.Label(root, text="History", font=("Segoe UI", 14), bg="#121212", fg="white").pack(pady=(20, 5))


history_text = tk.Text(root, height=8, bg="#1e1e1e", fg="white", font=("Segoe UI", 12), state=tk.DISABLED)
history_text.pack(padx=10, pady=5, fill='both', expand=True)

root.mainloop()
