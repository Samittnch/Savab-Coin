from tkinter import Tk, Label, Button

win= Tk() 



win.geometry("300x500")

win.title('ثواب کوین')


Label(win, text="ثواب کوین (لیست شدن در قیامت)", font=("BNazanin", 21),bg= "blue",fg= "green").pack()
global counter 
counter =0 
def  command0():
    global counter
    counter += 1 
    label1.config(text=counter)
def command1():
    global counter
    counter =- 500
    label1.config(text=counter)
Button(win , text='+ثواب' , command=command0).pack()
Button(win , text='گناه', command=command1).pack()
label1= Label(win,text='')
label1.pack()
win.mainloop()
