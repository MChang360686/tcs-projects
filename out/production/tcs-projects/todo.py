import tkinter as tk
from tkinter import messagebox


TASK_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        open(TASK_FILE, "w").close()

def save_tasks():
    with open(TASK_FILE, "w") as file:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def clear_tasks():
    task_listbox.delete(0, tk.END)
    save_tasks()

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

task_entry = tk.Entry(root, font=("Arial", 12), width=30)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", font=("Arial", 12), command=add_task)
add_button.pack(pady=5)

task_listbox = tk.Listbox(root, font=("Arial", 12), width=40, height=10)
task_listbox.pack(pady=10)

remove_button = tk.Button(root, text="Remove Task", font=("Arial", 12), command=remove_task)
remove_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All", font=("Arial", 12), command=clear_tasks)
clear_button.pack(pady=5)

load_tasks()

root.mainloop()
