from tkinter import *
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task != "":
        task_listbox.insert(END, task)
        entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    task_listbox.delete(ANCHOR)

window = Tk()
window.geometry('500x450+500+200')
window.title('Task Manager')
window.config(bg='#223441')
window.resizable(width=False, height=False)

frame = Frame(window)
frame.pack(pady=10)

task_listbox = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
)
task_listbox.pack(side=LEFT, fill=BOTH)

initial_tasks = [
    'Go to school',
    'Drink water',
    'Go to home',
    'Write code',
    'sleep',
    'Wake up',
    'Learn something new',
]

for task in initial_tasks:
    task_listbox.insert(END, task)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=BOTH)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

entry = Entry(
    window,
    font=('times', 24)
)
entry.pack(pady=20)

button_frame = Frame(window)
button_frame.pack(pady=20)

add_button = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=add_task
)
add_button.pack(fill=BOTH, expand=True, side=LEFT)

delete_button = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=delete_task
)
delete_button.pack(fill=BOTH, expand=True, side=LEFT)

window.mainloop()
