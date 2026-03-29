import tkinter as tk
gui = tk.Tk()
gui.title("College Form")
gui.geometry("400x350")
tk.Label(gui, text="Select your Subjects:").pack()
sub1 = tk.IntVar()
sub2 = tk.IntVar()
sub3 = tk.IntVar()
tk.Checkbutton(gui, text="Maths", variable=sub1).pack()
tk.Checkbutton(gui, text="Physics", variable=sub2).pack()
tk.Checkbutton(gui, text="Computer Science", variable=sub3).pack()
tk.Label(gui, text="Select your Department:").pack()
dept = tk.StringVar()
tk.Radiobutton(gui, text="CSE", variable=dept, value="CSE").pack()
tk.Radiobutton(gui, text="ECE", variable=dept, value="ECE").pack()
tk.Radiobutton(gui, text="EEE", variable=dept, value="EEE").pack()
def show_selection():
    subjects = []
    
    if sub1.get():
        subjects.append("Maths")
    if sub2.get():
        subjects.append("Physics")
    if sub3.get():
        subjects.append("Computer Science")
    
    result = "Subjects: " + ", ".join(subjects)
    result += "\nDepartment: " + dept.get()
    
    resultLabel.config(text=result)
tk.Button(gui, text="Submit", command=show_selection).pack()
resultLabel = tk.Label(gui, text="")
resultLabel.pack()
gui.mainloop()

