import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Log in Form")
root.geometry("400x350")
root.configure(bg="Blue")

title_label = tk.Label(
    root,
    text="USER LOGIN",
    font=("Arial",30,"bold"),
    bg="#26ac5a",
    fg="black"
)
title_label.pack(pady=5)

username_label = tk.Label(
    root,
    text="Username",
    font=("Arial",14),
    bg="#bc2942",
    fg="Black"
)
username_label.pack(pady=5)

username_entry = tk.Entry(
    root,
    font=("Arial",14),
    width=20
)
username_entry.pack(pady=5)


password_label = tk.Label(
    root,
    text="Password",
    font=("Arial",14),
    bg="#B7B729",
    fg="Black"
)
password_label.pack(pady=5)

password_entry = tk.Entry(
    root,
    font=("Arial",14),
    width=20,
    show="*"
)
password_entry.pack(pady=5)


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "12345": 
        messagebox.showinfo(
        "LOGIN SUCCESSFULLY!",
        "Welcome Admin!"
    )
    else:
        messagebox.showerror(
        "LOGIN FAILED",
        "Invalid Username and Password"
    )




login_button = tk.Button(
    root,
    text="LOG IN",
    font=("Arial",14,"bold"),
    bg="Blue",
    fg="White",
    width=25,
    command=login
)
login_button.pack(pady=20)


root.mainloop()