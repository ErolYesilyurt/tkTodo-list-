import tkinter as tk
from tkcalendar import Calendar

def add_task(name,listbox):
    task = text.get()
    if task:
        listbox.insert(tk.END,task)
        text.delete(0,tk.END)
        save_tasks(name,listbox)

def delete_task(name,listbox):
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        save_tasks(name,listbox)
    except IndexError:
        pass

def save_tasks(name,listbox):
    name1=get_selected_date()+name
    tasks = listbox.get(0, tk.END)
    with open(name1+".txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks(name,listbox):
    name1=get_selected_date()+name
    listbox.delete(0,tk.END)
    try:
        with open(name1+".txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

def move_tasks(name,listbox,listbox1):
    indexes=listbox.curselection()
    for index in indexes:
        value=listbox.get(index)
        listbox1.insert(tk.END,value)
        listbox.delete(index)
        save_tasks(name,listbox)
        save_tasks("tamamlananlar",listbox1)
    delete_spaces_in_completedtasks()
            
def delete_spaces_in_completedtasks():
    try:
        index = listbox1.get(0, tk.END).index("")
        listbox1.delete(index)  
    except ValueError:
        pass

    


def get_selected_date():
    return cal.get_date()


    


def load_all_tasks():
    load_tasks("gorevler",listbox)
    load_tasks("tamamlananlar",listbox1)

def delete_all_tasks():
    delete_task("gorevler",listbox)
    delete_task("tamamlananlar",listbox1)
   
     
    




window=tk.Tk()
window.geometry("700x400")
frameleft=tk.Frame(window,height=400,width=400,bg="dark green")
frameleft.pack(side="left",fill="both",expand=True)
frameright=tk.Frame(window,height=400,bg="dark green")
frameright.pack(side="left",fill="both",expand=True)

label=tk.Label(frameleft,text="Yapılacaklar",font=("Arial", 12, "bold"),bg=frameleft.cget("bg"),fg="white")
label.pack(side="top",padx=10)



listbox = tk.Listbox(frameleft, width=40, height=10, font=("Arial", 12),selectmode=tk.MULTIPLE)
listbox.pack(anchor="n", fill="both",padx=10,pady=10,expand=True)
scrollbar = tk.Scrollbar(listbox)
scrollbar.pack(side="right", fill="both")
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

label1=tk.Label(frameleft,text="Tamamlananlar",font=("Arial", 12, "bold"),bg=frameleft.cget("bg"),fg="white")
label1.pack(side="top",padx=10,pady=10)
listbox1 = tk.Listbox(frameleft, width=40, height=10, font=("Arial", 12),selectmode=tk.MULTIPLE)
listbox1.pack(anchor="n", fill="both",padx=10,pady=10,expand=True)
scrollbar1 = tk.Scrollbar(listbox1)
scrollbar1.pack(side="right", fill="both")
listbox1.config(yscrollcommand=scrollbar1.set)
scrollbar1.config(command=listbox1.yview)



text=tk.Entry(frameleft)
text.pack(side="left",fill="x",padx=10,expand=True)

badd=tk.Button(frameleft,text="ekle",command=lambda:add_task("gorevler",listbox))
badd.pack(side="left",padx=10)

bdel=tk.Button(frameleft,text="sil",command=lambda:delete_all_tasks())
bdel.pack(side="left",padx=10,pady=10)

bsetgreen=tk.Button(frameleft,text="isretle",command=lambda:move_tasks("gorevler",listbox,listbox1))
bsetgreen.pack(anchor="sw",padx=10,pady=10)

cal = Calendar(frameright, selectmode="day", date_pattern="y-mm-dd",locale="tr_TR")
cal.pack(padx=10,pady=10)

cal.bind("<<CalendarSelected>>", lambda event: load_all_tasks())




load_all_tasks()
window.mainloop()
   