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
root.title("Social Calendar")
root.geometry('805x505')
img=PhotoImage(file=r"C:\Users\gonel\OneDrive\Desktop\Desktop Folders\Project\pic1.png",master=root)
img_label=Label(root,image=img)
img_label.place(x=0,y=0)

def adminpg():
    global root
    root=Tk()
    root.config(background='white')
    img1=PhotoImage(file=r"C:\Users\gonel\OneDrive\Desktop\Desktop Folders\Project\pic4.png",master=root)
    img1_label=Label(root,image=img1)
    img1_label.place(x=0,y=0)
    root.title('Login Page')
    root.geometry('800x500')
    inp=Label(root,text='Password')
    inp.place(relx=0.4,rely=0.5)
    
    global pwd
    pwd= Entry(root,show="*",width=20)
    pwd.pack()
    pwd.place(relx=0.5,rely=0.5)
    t=pwd.get()
    if t == '123456':
        btn1 = Button(root, text = 'Login', bd = '6',command =DBdet)
        btn1.place(relx=0.5, rely=0.7, anchor='center')
    else:
        btn1 = Button(root, text = 'Login', bd = '6',command =DBdet)
        btn1.place(relx=0.5, rely=0.7, anchor='center')
    root.mainloop()
        
def userpg():
    root7=Tk()
    root7.geometry('800x500')
    root7.title('User options')
    root7.config(background='white')
    img1=PhotoImage(file=r"C:\Users\gonel\OneDrive\Desktop\Desktop Folders\Project\pic2.png",master=root7)
    img1_label=Label(root7,image=img1)
    img1_label.place(x=0,y=0)
    btn1 = Button(root7, text = 'All Birthdays', bd = '6',command =allbdays)
    btn1.place(relx=0.5, rely=0.4, anchor='center')
    btn2 = Button(root7, text = 'Specific Birthdays', bd = '6',command =specbdays)
    btn2.place(relx=0.5, rely=0.5, anchor='center')
    root7.mainloop()
    
def allbdays():
    st="SELECT * FROM Birthdays"
    cur.execute(st)
    d=cur.fetchall()
    if d==[]:
        messagebox.showinfo("Attention", "No Birthdays present in the table")
    else:
        class Table:
        	def __init__(self,root9):
        		for i in range(total_rows):
        			for j in range(total_columns):
        				self.e = Entry(root9, width=20, fg='black',font=('Arial',12))
        				self.e.grid(row=i, column=j)
        				self.e.insert(END, d[i][j])
        total_rows = len(d)
        total_columns = len(d[0])
        root9 = Tk()
        root9.title('Details')
        t = Table(root9)
        root9.mainloop()

def specbdays():
    root1 = Tk()
    root1.geometry("400x300")
    cal = Calendar(root1, selectmode = 'day',year = 2023, month = 1,day = 1)
    cal.pack(pady = 20)
    global d1
    d1={'1':'January','2':'February','3':'March','4':'April','5':'May',
        '6':'June','7':'July','8':'August',
        '9':'September','10':'October','11':'November','12':'December'}
    def getbday():
        yu=cal.get_date().split('/')
        y=d1[yu[0]]
        z=(yu[1])
        st="SELECT * FROM Birthdays WHERE Birthday_Month='{}' and Birthday_Date={}".format(d1[yu[0]],yu[1])
        cur.execute(st)
        d=cur.fetchall()
        if d==[]:
            messagebox.showinfo("Info", "No Birthdays on the selected date")
        else:
            class Table:
            	def __init__(self,root10):
            		for i in range(total_rows):
            			for j in range(total_columns):            				
            				self.e = Entry(root10, width=20, fg='black',font=('Arial',12))
            				self.e.grid(row=i, column=j)
            				self.e.insert(END, d[i][j])
            total_rows = len(d)
            total_columns = len(d[0])
            root10 = Tk()
            root10.title('Specific Birthday')
            t = Table(root10)
            root10.mainloop()

    Button(root1, text = "Get Birthdays",command=getbday).pack(pady = 20)
    
    date = Label(root1, text = "")
    date.pack(pady = 20)

    root1.mainloop()

def DBdet():
    t=pwd.get()
    try:    
        if t=='123456':
            root2 = Tk()
            root2.title("Database Details")
            root2.geometry("800x500")
            root2.config(background='white')
            img1=PhotoImage(file=r"C:\Users\gonel\OneDrive\Desktop\Desktop Folders\Project\pic2.png",master=root2)
            img1_label=Label(root2,image=img1)
            img1_label.place(x=0,y=0)
            
            inp1=Label(root2,text='Enter hostname')
            inp2=Label(root2,text='Enter Username of Mysql')
            inp3=Label(root2,text='Enter Password')
            inp4=Label(root2,text='Enter Database name')
            inp1.place(relx=0.1,rely=0.1)
            inp2.place(relx=0.1,rely=0.5)
            inp3.place(relx=0.5,rely=0.1)
            inp4.place(relx=0.5,rely=0.5)
            global ent1 
            global ent2
            global ent3
            global ent4
            ent1=Entry(root2,width=25)
            ent2=Entry(root2,width=25)
            ent3=Entry(root2,show="*",width=25)
            ent4=Entry(root2,width=25)
            
            ent1.place(relx=0.25,rely=0.1)
            ent2.place(relx=0.3,rely=0.5)
            ent3.place(relx=0.65,rely=0.1)
            ent4.place(relx=0.7,rely=0.5)
            btn5= Button(root2, text = 'Submit', bd = '6',command=DBconnect)
            btn5.place(relx=0.5, rely=0.7, anchor='center')        
            root2.mainloop()
        else:
            inp=Label(root,text='Invalid Admin Password')
            inp.place(relx=0.4,rely=0.6)
    except:
        inp=Label(root,text='Invalid Admin Password')
        inp.place(relx=0.5,rely=0.5) 

def DBconnect():
    e1=ent1.get()
    e2=ent2.get()
    e3=ent3.get()
    e4=ent4.get()
    try:
        myconn = mysq.connect(host=e1,user=e2,passwd=e3,database=e4)
        cur=myconn.cursor()
        if myconn.is_connected:    
            messagebox.showinfo("Connection Status", "Successfully Connected")
            root4=Tk()
            root4.title('Admin Options')
            img1=PhotoImage(file=r"C:\Users\gonel\OneDrive\Desktop\Desktop Folders\Project\pic6.png",master=root4)
            img1_label=Label(root4,image=img1)
            img1_label.place(x=0,y=0)
            root4.geometry('800x500')
            btn4 = Button(root4, text = 'Display All Bdays', bd = '6',command = adallbday)
            btn4.place(relx=0.5, rely=0.1, anchor='center')
            btn1 = Button(root4, text = 'Add records', bd = '6',command = addrec)
            btn1.place(relx=0.5, rely=0.3, anchor='center')
            btn2 = Button(root4, text = 'Delete records', bd = '6',command = delrec1)
            btn2.place(relx=0.5, rely=0.5, anchor='center')
            btn3 = Button(root4, text = 'Update records', bd = '6',command = updrec1)
            btn3.place(relx=0.5, rely=0.7, anchor='center')
            root4.mainloop()           
    except:
        messagebox.showinfo("Connection Status", "Invalid Credentials")

def adallbday():
    st="SELECT * FROM Birthdays"
    cur.execute(st)
    d=cur.fetchall()
    if d==[]:
        messagebox.showinfo("Attention", "No Birthdays present in the table")
    else:
        class Table:
        	def __init__(self,root9):
        		for i in range(total_rows):
        			for j in range(total_columns):        				
        				self.e = Entry(root9, width=20, fg='black',font=('Arial',12))
        				self.e.grid(row=i, column=j)
        				self.e.insert(END, d[i][j])
        total_rows = len(d)
        total_columns = len(d[0])
        root9 = Tk()
        root9.title('Details')
        t = Table(root9)
        root9.mainloop()

def addrec():
    root=Tk()
    root.config(background='white')
    img1=PhotoImage(file=r"C:\Users\gonel\OneDrive\Desktop\Desktop Folders\Project\pic7.png",master=root)
    img1_label=Label(root,image=img1)
    img1_label.place(x=0,y=0)
    root.title('Admin Page')
    root.geometry('800x500')
    inp1=Label(root,text='Enter ID')
    inp2=Label(root,text='Name')
    inp3=Label(root,text='BDay_Month')
    inp4=Label(root,text='BDay_Date')
        
    inp1.place(relx=0.2,rely=0.2)
    inp2.place(relx=0.2,rely=0.4)
    inp3.place(relx=0.5,rely=0.2)
    inp4.place(relx=0.5,rely=0.4)
    
    global txt1
    global txt2
    global txt3
    global txt4
    
    txt1=Entry(root,width=20)
    txt2=Entry(root,width=20)
    txt3=Entry(root,width=20)
    txt4=Entry(root,width=20)
    
    txt1.place(relx=0.3,rely=0.2)
    txt2.place(relx=0.3,rely=0.4)
    txt3.place(relx=0.65,rely=0.2)
    txt4.place(relx=0.65,rely=0.4)
                
    btn1 = Button(root, text = 'Submit', bd = '6',command = insrt)
    btn1.place(relx=0.5, rely=0.6, anchor='center')
    root.mainloop()

def insrt():
    t1=txt1.get()
    t2=txt2.get()
    t3=txt3.get()
    t4=txt4.get()
    st="""INSERT INTO Birthdays(ID,Name,Birthday_Month,Birthday_Date) 
                       VALUES({},'{}','{}',{})""".format(t1,t2,t3,t4)
    cur.execute(st)
    cnx.commit()
    messagebox.showinfo("Status", "Inserted records successfully")
    
def delrec1():
    root5=Tk()
    img1=PhotoImage(file=r"C:\Users\gonel\OneDrive\Desktop\Desktop Folders\Project\pic7.png",master=root5)
    img1_label=Label(root5,image=img1)
    img1_label.place(x=0,y=0)
    root5.title('Delete record')
    root5.geometry('800x500')
    root5.config(background='white')
    inp1=Label(root5,text='Enter ID of the teacher to delete:')
    inp1.place(relx=0.4,rely=0.5,anchor='center')
    global text1
    text1=Entry(root5,width=20)
    text1.place(relx=0.6,rely=0.5,anchor='center')
    btn1 = Button(root5, text = 'Submit', bd = '6',command = delrec2)
    btn1.place(relx=0.5, rely=0.7, anchor='center')
    root5.mainloop()
    
def delrec2():
    t=text1.get()
    st="DELETE FROM Birthdays where Id={}".format(t)
    cur.execute(st)
    cnx.commit()
    messagebox.showinfo("Status", "Deleted records successfully")

def updrec1():
    root6=Tk()
    root6.title('Update record')
    root6.geometry('800x500')
    img1=PhotoImage(file=r"C:\Users\gonel\OneDrive\Desktop\Desktop Folders\Project\pic7.png",master=root6)
    img1_label=Label(root6,image=img1)
    img1_label.place(x=0,y=0)
    root6.config(background='white')
    inp1=Label(root6,text='Enter ID of the teacher to update:')
    inp1.place(relx=0.4,rely=0.3,anchor='center')
    inp2=Label(root6,text='Enter field to update:')
    inp2.place(relx=0.4,rely=0.5,anchor='center')
    inp3=Label(root6,text='Enter updated value:')
    inp3.place(relx=0.4,rely=0.7,anchor='center')
    global tt1
    global tt2
    global tt3
    tt1=Entry(root6,width=20)
    tt1.place(relx=0.6,rely=0.3,anchor='center')
    tt2=Entry(root6,width=20)
    tt2.place(relx=0.6,rely=0.5,anchor='center')
    tt3=Entry(root6,width=20)
    tt3.place(relx=0.6,rely=0.7,anchor='center')
    btn1 = Button(root6, text = 'Submit', bd = '6',command = updrec2)
    btn1.place(relx=0.5, rely=0.8, anchor='center')
    root6.mainloop()
    
def updrec2():
    t1t=tt1.get()
    t2t=tt2.get()
    t3t=tt3.get()
    st="UPDATE Birthdays SET Birthday_Month='{}' WHERE Id={} ".format(t3t,t1t)
    cur.execute(st)
    cnx.commit()
    messagebox.showinfo("Status", "Updated records successfully")

btn1 = Button(root, text = 'Admin mode', bd = '6',command = adminpg)
btn2 = Button(root, text = 'User mode', bd = '6',command = userpg)
btn1.place(relx=0.5, rely=0.5, anchor='center')
btn2.place(relx=0.5, rely=0.4, anchor='center')

root.mainloop()