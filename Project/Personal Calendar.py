from tkinter import *
from tkcalendar import Calendar
from PIL import ImageTk
import mysql.connector as mysq
from tkinter import messagebox

root = Tk()
global cnx
global cur
cnx = mysq.connect(user='root', passwd='password',host='localhost',database='CSProject')
cur=cnx.cursor()
root.title("Personal Calendar")
root.geometry('805x505')
img=PhotoImage(file=r"C:\Users\gonel\OneDrive\Desktop\Desktop Folders\Surya\pic1.png",master=root)
img_label=Label(root,image=img)
img_label.place(x=0,y=0)

def inp_cal():
    global root
    root=Tk()
    root.config(background='white')
    img1=PhotoImage(file=r"C:\Users\gonel\OneDrive\Desktop\Desktop Folders\Surya\pic4.png",master=root)
    img1_label=Label(root,image=img1)
    img1_label.place(x=0,y=0)
    root.title('Personal Calendar')
    root.geometry('800x500')
    inp=Label(root,text='Month')
    inp.place(relx=0.4,rely=0.5)
    
    global data
    data= Entry(root,width=20)
    data.pack()
    data.place(relx=0.5,rely=0.5)
    t=data.get()
    if t == '123456':
        btn1 = Button(root, text = 'Login', bd = '6',command =DBdet)
        btn1.place(relx=0.5, rely=0.7, anchor='center')
    else:
        btn1 = Button(root, text = 'Login', bd = '6',command =DBdet)
        btn1.place(relx=0.5, rely=0.7, anchor='center')
    root.mainloop()
    