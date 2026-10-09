import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected_index = task_listbox.curselection()
        task_listbox.delete(selected_index[0])
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Main application window
root = tk.Tk()
root.title("Omar's Task Manager")
root.geometry("400x450")

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

# Delete button
delete_button = tk.Button(root, text="Delete Selected Task", command=delete_task, bg="#f44336", fg="white", font=("Arial", 10, "bold"))
delete_button.pack(pady=5)

root.mainloop()