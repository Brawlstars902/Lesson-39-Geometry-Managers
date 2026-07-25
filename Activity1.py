from tkinter import *
window = Tk()
window.title('Activity 1')
window.geometry('300x300')

f1 = Frame(master = window, bg = 'yellow',height= 50, width= 50)
f1.pack()

btn = Button(master = f1,text = 'Click here',bg = 'red')
btn.pack()

f2 = Frame(master = window, bg = 'blue',height= 100,width = 200)
f2.pack()

window.mainloop()