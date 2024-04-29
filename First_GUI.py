import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

COLOR1 = "Blue"
COLOR2 = "Gold"
COLOR3 = "Red"

scrol_w = 30
scrol_h = 3

def radCall():
    radSel = radVar.get()
    if radSel == 1: win.configure(background=COLOR1)
    elif radSel == 2: win.configure(background=COLOR2)
    elif radSel == 3: win.configure(background=COLOR3)
    



    
    

def click_me():
    action.configure(text='Hello  '+ name.get()+ number.get())
    
win = tk.Tk()
win.title('Python GUI')
a_label = ttk.Label(win,text = 'A Label')
a_label.grid(column=0,row=0)
action = ttk.Button(win,text= "Click me", command = click_me)
action.grid(column=2,row=1)   

radVar =tk.IntVar()

rad1 = tk.Radiobutton(win,text=COLOR1, variable=radVar, value=1, command=radCall)
rad1.grid(column=0,row=5,sticky=tk.W, columnspan=3)

rad2 = tk.Radiobutton(win,text=COLOR2, variable=radVar, value=2, command=radCall)
rad2.grid(column=1,row=5,sticky=tk.W, columnspan=3)

rad3 = tk.Radiobutton(win,text=COLOR3, variable=radVar, value=3, command=radCall)
rad3.grid(column=2,row=5,sticky=tk.W, columnspan=3)


ttk.Label(win,text ="Choose a number:").grid(column = 1, row =0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win,width=12,textvariable=number)
number_chosen['values'] = (1,2,4,42,100)
number_chosen.grid(column=1,row=1)
number_chosen.current(1)

name = tk.StringVar()
name_entered = ttk.Entry(win,width= 12, textvariable=name)
name_entered.grid(column=0,row=1)

scr = scrolledtext.ScrolledText(win,width=scrol_w, height = scrol_h, wrap=tk.WORD)
scr.grid(column=0,columnspan=10)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win,text="Disabled",variable=chVarDis,state='disabled')
check1.select()
check1.grid(column=0,row=4,sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win,text="Unchecked",variable=chVarUn)
check2.deselect()
check2.grid(column=1,row=4,sticky=tk.W)


chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win,text="Enabled",variable=chVarEn)
check3.select()
check3.grid(column=2,row=4,sticky=tk.W)





name_entered.focus()

    
win.mainloop()