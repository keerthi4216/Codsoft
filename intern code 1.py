import tkinter as tk
from tkinter import messagebox
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks():
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

def add_task():
    task = entry.get().strip()
    if task:
        tasks.append({"task": task, "done": False})
        save_tasks()
        entry.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def mark_done(index):
    tasks[index]["done"] = not tasks[index]["done"]
    save_tasks()
    update_task_list()

def delete_task(index):
    del tasks[index]
    save_tasks()
    update_task_list()

def update_task_list():
    for widget in task_frame.winfo_children():
        widget.destroy()

    for idx, item in enumerate(tasks):
        status = "✔️" if item["done"] else "❌"
        task_label = tk.Label(task_frame, text=f"{status} {item['task']}", anchor="w")
        task_label.grid(row=idx, column=0, sticky="w")

        done_btn = tk.Button(task_frame, text="Done", command=lambda i=idx: mark_done(i))
        done_btn.grid(row=idx, column=1)

        del_btn = tk.Button(task_frame, text="Delete", command=lambda i=idx: delete_task(i))
        del_btn.grid(row=idx, column=2)

# Main Window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

# Task Entry
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack(pady=5)

# Task List Frame
task_frame = tk.Frame(root)
task_frame.pack(pady=10)

# Load tasks from file
tasks = load_tasks()
update_task_list()

# Run the app
root.mainloop()
