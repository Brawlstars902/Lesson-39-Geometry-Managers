from tkinter import *

root = Tk()
root.title('Login App')
root.geometry('400x400')

frame = Frame(master = root, bg = 'yellow', height = 200, width = 360)

lbl_1 = Label(text = 'Full Name', bg = 'blue', width = 12)
lbl_2 = Label(text = 'Email Address', bg = 'blue', width = 12)
lbl_3 = Label(text = 'Password', bg = 'blue', width = 12)

name_entry = Entry(frame)
email_entry = Entry(frame)
password_entry = Entry(frame)

def display():
    name = name_entry.get()
    greet = 'Hello '+name+'\n'
    message = 'Congratulations for the new account!'
    text_box.insert(END,greet)
    text_box.insert(END,message)

text_box = Text(bg = '#BEBEBE', fg = 'black')

btn = Button(text = 'Create Account', command = display, bg = 'red')

frame.place(x = 20,y = 0)
lbl_1.place(x = 20,y = 20)
name_entry.place(x = 150,y = 20)
lbl_2.place(x = 20,y = 80)
email_entry.place(x = 150,y =80)
lbl_3.place(x = 20,y = 140)
password_entry.place(x = 150,y = 140)
btn.place(x = 130,y = 210)
text_box.place(y = 250)

root.mainloop()