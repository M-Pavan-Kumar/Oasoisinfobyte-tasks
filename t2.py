import tkinter as tk
import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_numbers=True, use_symbols=True):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

def generate_and_display_password():
    length = int(length_entry.get())
    use_uppercase = uppercase_var.get() == 1
    use_lowercase = lowercase_var.get() == 1
    use_numbers = numbers_var.get() == 1
    use_symbols = symbols_var.get() == 1

    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols)
    password_display.config(state=tk.NORMAL)
    password_display.delete(1.0, tk.END)
    password_display.insert(tk.END, password)
    password_display.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Random Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

uppercase_var = tk.IntVar()
uppercase_checkbutton = tk.Checkbutton(root, text="Uppercase Letters", variable=uppercase_var)
uppercase_checkbutton.grid(row=1, column=0, columnspan=2, sticky=tk.W)

lowercase_var = tk.IntVar()
lowercase_checkbutton = tk.Checkbutton(root, text="Lowercase Letters", variable=lowercase_var)
lowercase_checkbutton.grid(row=2, column=0, columnspan=2, sticky=tk.W)

numbers_var = tk.IntVar()
numbers_checkbutton = tk.Checkbutton(root, text="Include Numbers", variable=numbers_var)
numbers_checkbutton.grid(row=3, column=0, columnspan=2, sticky=tk.W)

symbols_var = tk.IntVar()
symbols_checkbutton = tk.Checkbutton(root, text="Include Symbols", variable=symbols_var)
symbols_checkbutton.grid(row=4, column=0, columnspan=2, sticky=tk.W)

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.grid(row=5, column=0, columnspan=2)

password_display = tk.Text(root, height=1, width=30, state=tk.DISABLED)
password_display.grid(row=6, column=0, columnspan=2)

root.mainloop()
