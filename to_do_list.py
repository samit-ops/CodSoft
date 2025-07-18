import tkinter as tk
from tkinter import ttk, messagebox

# Master Task List
tasks = []

# Initialize main window
root = tk.Tk()
root.title("🔥 Techy To-Do List")
root.geometry("500x680")
root.config(bg="#1c1c1c")
root.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")

# Entry Frame
entry_frame = tk.Frame(root, bg="#1c1c1c")
entry_frame.pack(pady=20)

task_entry = ttk.Entry(entry_frame, width=30, font=("Segoe UI", 14))
task_entry.grid(row=0, column=0, padx=10)

def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append({"text": task, "status": "Pending"})
        task_entry.delete(0, tk.END)
        refresh_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

add_btn = tk.Button(entry_frame, text="➕ Add Task", font=("Segoe UI", 12),
                    bg="#00ADB5", fg="white", relief="flat", bd=0,
                    command=add_task, height=1, width=10)
add_btn.grid(row=0, column=1, padx=10)

# Filter Frame
filter_frame = tk.Frame(root, bg="#1c1c1c")
filter_frame.pack()

current_filter = tk.StringVar(value="All")

def set_filter(f):
    current_filter.set(f)
    refresh_tasks()

filters = ["All", "Pending", "Completed"]
for i, f in enumerate(filters):
    tk.Radiobutton(filter_frame, text=f, variable=current_filter, value=f,
                   font=("Segoe UI", 11), bg="#1c1c1c", fg="white", selectcolor="#00ADB5",
                   activebackground="#1c1c1c", activeforeground="#00ADB5",
                   command=lambda f=f: set_filter(f)).grid(row=0, column=i, padx=15)

# Task Display Frame
task_frame = tk.Frame(root, bg="#1c1c1c")
task_frame.pack(pady=10, fill="both", expand=True)

def toggle_status(index):
    task = tasks[index]
    task["status"] = "Completed" if task["status"] == "Pending" else "Pending"
    refresh_tasks()

def delete_task(index):
    del tasks[index]
    refresh_tasks()

def refresh_tasks():
    for widget in task_frame.winfo_children():
        widget.destroy()

    for idx, task in enumerate(tasks):
        if current_filter.get() != "All" and task["status"] != current_filter.get():
            continue

        bg_color = "#FFD369" if task["status"] == "Pending" else "#32e0c4"
        fg_color = "#000000" if task["status"] == "Pending" else "#ffffff"
        btn_bg = "#393E46" if task["status"] == "Pending" else "#222831"

        task_row = tk.Frame(task_frame, bg=bg_color, pady=5)
        task_row.pack(fill="x", padx=10, pady=4)

        tk.Label(task_row, text=task["text"], font=("Segoe UI", 13),
                 bg=bg_color, fg=fg_color, anchor="w").pack(side="left", fill="x", expand=True, padx=10)

        tk.Button(task_row, text="✓" if task["status"] == "Pending" else "↩",
                  font=("Segoe UI", 10), width=3, bg=btn_bg, fg="white", bd=0,
                  command=lambda i=idx: toggle_status(i)).pack(side="right", padx=4)

        tk.Button(task_row, text="🗑", font=("Segoe UI", 10), width=3,
                  bg="#D72323", fg="white", bd=0,
                  command=lambda i=idx: delete_task(i)).pack(side="right", padx=4)

# Animated Footer
footer_frame = tk.Frame(root, bg="#1c1c1c")
footer_frame.pack(pady=(5, 10))

footer_text = "Made by SAMIT "
text_label = tk.Label(footer_frame, text=footer_text, font=("Segoe UI", 10), bg="#1c1c1c", fg="#AAAAAA")
heart_label = tk.Label(footer_frame, text="❤️", font=("Segoe UI", 10), bg="#1c1c1c", fg="#FF6B81")

text_label.pack(side="left")
heart_label.pack(side="left")

# Heart pulse animation
def pulse(size=10, growing=True):
    new_size = size + 1 if growing else size - 1
    heart_label.config(font=("Segoe UI", new_size))
    if new_size >= 14:
        growing = False
    elif new_size <= 10:
        growing = True
    root.after(200, pulse, new_size, growing)

pulse()  # Start the animation

# Start App
refresh_tasks()
root.mainloop()