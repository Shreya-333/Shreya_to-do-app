import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# ---------- Emoji Function ----------
def emoji_for_task(task):
    task = task.lower()
    if "study" in task or "homework" in task:
        return "📚"
    elif "meeting" in task or "call" in task:
        return "📞"
    elif "shop" in task or "buy" in task:
        return "🛒"
    elif "birthday" in task or "party" in task:
        return "🎉"
    elif "walk" in task or "exercise" in task:
        return "🏃"
    else:
        return "✅"

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("ShreyaTasks - Personal To-Do Manager")
root.geometry("450x500")
root.configure(bg="#f0f8f9")

tasks = []

# ---------- Add Task ----------
def add_task():
    task = task_input.get()
    if task.strip():
        time_added = datetime.now().strftime("%d %b %Y %I:%M %p")
        emoji = emoji_for_task(task)
        tasks.append({"task": f"{emoji} {task}", "time": time_added})
        update_listbox()
        task_input.delete(0, tk.END)
    else:
        messagebox.showwarning("Oops!", "Task cannot be empty")

# ---------- Delete Task ----------
def delete_task():
    try:
        index = task_list.curselection()[0]
        tasks.pop(index)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Oops!", "Please select a task to delete.")

# ---------- Update Listbox ----------
def update_listbox():
    task_list.delete(0, tk.END)
    for item in tasks:
        task_list.insert(tk.END, f"{item['task']} ({item['time']})")

# ---------- Widgets ----------
task_input = tk.Entry(root, font=("segoe ui", 14), width=30, bd=2, relief="groove")
task_input.pack(pady=10)

btn_frame = tk.Frame(root, bg="#f0f8f9")
btn_frame.pack()

tk.Button(btn_frame, text="Add", font=("segoe ui", 12), command=add_task).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Delete", font=("segoe ui", 12), command=delete_task).pack(side=tk.LEFT, padx=5)

task_list = tk.Listbox(root, width=50, height=15, font=("segoe ui", 12), bd=2)
task_list.pack(pady=20)

root.mainloop()
