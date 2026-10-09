import tkinter as tk
from tkinter import messagebox
import json
import os

FILENAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as file:
                tasks = json.load(file)
                for task in tasks:
                    task_listbox.insert(tk.END, task)
        except json.JSONDecodeError:
            pass

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open(FILENAME, "w") as file:
        json.dump(list(tasks), file)

def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected_index = task_listbox.curselection()
        task_listbox.delete(selected_index[0])
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def complete_task():
    try:
        selected_index = task_listbox.curselection()
        task_text = task_listbox.get(selected_index)
        # Check if already marked complete
        if not task_text.startswith("✔ "):
            task_listbox.delete(selected_index)
            task_listbox.insert(selected_index, f"✔ {task_text}")
            save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to complete.")

# Main application window
root = tk.Tk()
root.title("Omar's Task Manager - Pro Edition")
root.geometry("400x500")

# Input frame
entry_frame = tk.Frame(root)
entry_frame.pack(pady=15)

task_entry = tk.Entry(entry_frame, width=22, font=("Arial", 14))
task_entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(entry_frame, text="Add Task", command=add_task, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
add_button.pack(side=tk.LEFT)

# Task list view
task_listbox = tk.Listbox(root, width=32, height=14, font=("Arial", 12))
task_listbox.pack(pady=10)

# Action buttons frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

complete_button = tk.Button(btn_frame, text="Complete", command=complete_task, bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
complete_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(btn_frame, text="Delete", command=delete_task, bg="#f44336", fg="white", font=("Arial", 10, "bold"))
delete_button.pack(side=tk.LEFT, padx=5)

# Load saved tasks on startup
load_tasks()

root.mainloop()