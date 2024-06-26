from tkinter import *
def click(event):
    text=event.widget.cget("text")
    print(text)
    screen.update()
    if text=="=":                               #gives value
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(scvalue.get())
            except Exception as e:              #handles any kind of errors
                scvalue.set("Error")
                screen.update()
                print(e)
        scvalue.set(value)
        screen.update()
        
    elif text=="C":                             #clear button
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

root=Tk()                                       #GUI
root.geometry("380x600")
root.title("Calculator By Shreyas")
root.iconbitmap('calculator_3534.ico')
root.resizable(False,False)
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvariable=scvalue,font="lucida 40 bold")
screen.pack(fill=X,padx=18,pady=18)
f=Frame(root,background="grey")
b=Button(f,text="7",font="lucida 30 bold")
b.pack(padx=12,pady=7,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="8",font="lucida 30 bold")
b.pack(padx=7,pady=7,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="9",font="lucida 30 bold")
b.pack(padx=7,pady=7,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="-",font="lucida 30 bold")
b.pack(padx=7,pady=7,side=LEFT)
b.bind("<Button-1>",click)

f.pack()
f=Frame(root,background="grey")
b=Button(f,text="4",font="lucida 30 bold")
b.pack(padx=7,pady=7,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="5",font="lucida 30 bold")
b.pack(padx=7,pady=7,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="6",font="lucida 30 bold")
b.pack(padx=7,pady=7,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="+",font="lucida 30 bold")
b.pack(padx=7,pady=7,side=LEFT)
b.bind("<Button-1>",click)

f.pack()
f=Frame(root,background="grey")
b=Button(f,text="1",font="lucida 30 bold")
b.pack(padx=7,pady=7,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="2",font="lucida 30 bold")
b.pack(padx=7,pady=7,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="3",font="lucida 30 bold")
b.pack(padx=7,pady=7,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="=",font="lucida 30 bold")
b.pack(padx=7,pady=7,side=LEFT)
b.bind("<Button-1>",click)


f.pack()
f=Frame(root,background="grey")
b=Button(f,text="0",font="lucida 30 bold")
b.pack(padx=8,pady=7,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text=".",font="lucida 30 bold")
b.pack(padx=7,pady=7,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="*",font="lucida 30 bold")
b.pack(padx=7,pady=7,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="%",font="lucida 30 bold")
b.pack(padx=9,pady=7,side=LEFT)
b.bind("<Button-1>",click)


f.pack()
f=Frame(root,background="grey")
b=Button(f,text="C",font="lucida 30 bold")
b.pack(padx=7,pady=7,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="(",font="lucida 30 bold")
b.pack(padx=11,pady=7,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text=")",font="lucida 30 bold")
b.pack(padx=10,pady=7,side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="/",font="lucida 30 bold")
b.pack(padx=11,pady=7,side=LEFT)
b.bind("<Button-1>",click)



f.pack()

root.mainloop()