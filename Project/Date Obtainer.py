# Import Required Library
from tkinter import *
from tkcalendar import Calendar

# Create Object
root = Tk()

d={'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August',
   '9':'September','10':'October','11':'November','12':'December'}

# Set geometry
root.geometry("400x400")

# Add Calendar
cal = Calendar(root, selectmode = 'day',
			year = 2020, month = 5,
			day = 22)

cal.pack(pady = 20)

def grad_date():
    print(cal.get_date())
    yu=cal.get_date().split('/')
    print(yu)
    y=d[yu[0]]
    
# Add Button and Label
Button(root, text = "Get Date",
	command = grad_date).pack(pady = 20)

date = Label(root, text = "")
date.pack(pady = 20)

# Execute Tkinter
root.mainloop()
