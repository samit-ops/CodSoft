import tkinter as tk
from tkinter import ttk
import string
import random

# Function to generate password
def generate_password():
    try:
        length = int(length_var.get())
        if length <= 0:
            raise ValueError

        characters = ""
        if use_upper.get(): characters += string.ascii_uppercase
        if use_lower.get(): characters += string.ascii_lowercase
        if use_digits.get(): characters += string.digits
        if use_special.get(): characters += string.punctuation

        if not characters:
            output_var.set("Choose at least one character set!")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        output_var.set(password)

    except ValueError:
        output_var.set("Enter a valid length!")

# App setup
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("450x500")
root.config(bg="#1e272e")

# Styles
style = ttk.Style()
style.configure("TCheckbutton", background="#1e272e", foreground="white", font=("Segoe UI", 11))
style.configure("TLabel", background="#1e272e", foreground="white", font=("Segoe UI", 12))

# Heading
title = tk.Label(root, text="🔐 Password Generator", font=("Segoe UI", 20, "bold"), fg="#00cec9", bg="#1e272e")
title.pack(pady=20)

# Frame for content
content = tk.Frame(root, bg="#1e272e")
content.pack(pady=10)

# Length input
ttk.Label(content, text="Password Length:").grid(row=0, column=0, pady=5, sticky='w')
length_var = tk.StringVar(value="12")
length_entry = ttk.Entry(content, textvariable=length_var, width=10)
length_entry.grid(row=0, column=1, pady=5, sticky='w')

# Character options
use_upper = tk.BooleanVar(value=True)
use_lower = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_special = tk.BooleanVar(value=False)

ttk.Checkbutton(content, text="Include Uppercase (A-Z)", variable=use_upper).grid(row=1, column=0, columnspan=2, sticky='w')
ttk.Checkbutton(content, text="Include Lowercase (a-z)", variable=use_lower).grid(row=2, column=0, columnspan=2, sticky='w')
ttk.Checkbutton(content, text="Include Numbers (0-9)", variable=use_digits).grid(row=3, column=0, columnspan=2, sticky='w')
ttk.Checkbutton(content, text="Include Special (!@#...)", variable=use_special).grid(row=4, column=0, columnspan=2, sticky='w')

# Generate button
generate_btn = tk.Button(root, text="Generate Password", command=generate_password,
                         font=("Segoe UI", 12, "bold"), bg="#00b894", fg="white", width=20)
generate_btn.pack(pady=20)

# Output field
output_var = tk.StringVar()
output_label = tk.Label(root, textvariable=output_var, font=("Courier New", 14, "bold"), fg="#dfe6e9", bg="#1e272e", wraplength=400)
output_label.pack(pady=10)

# Footer
tk.Label(root, text="Built with Python 💻", font=("Segoe UI", 10), fg="#636e72", bg="#1e272e").pack(pady=10)

# Run App
root.mainloop()