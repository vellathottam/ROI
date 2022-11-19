from tkinter import *
from tkinter import messagebox
import webbrowser



window=Tk()


def mkat():
    global absentlist
    absentlist=[1,11,45,2,3,4,5]
    li=str(absentlist)[1:-1]
    varabsent.set(li)

def open():
    webbrowser.open('https://vellathottam.github.io')



#menubar and menu options

menubar=Menu(window)

submenu = Menu(menubar, tearoff =0)
submenu.add_command(label = 'Record Attendance')
submenu.add_command(label = 'Mark Attendance', command = mkat)

attendance = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Attendance', menu = attendance)
attendance.add_cascade(label = 'Take Attendance', menu = submenu)
attendance.add_command(label = 'View Attendance')

alert = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Alert', menu = alert)
alert.add_command(label = 'Send Alert')

help = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Help', menu = help)
help.add_command(label = 'Get Help', command = open)
help.add_separator()
help.add_command(label = 'About ROI', command = None)


#entry and labels

varstaffid = StringVar()
label_a=Label(window, text='Staff ID', font="Cambria")
label_a.place(x=100, y=199)
staffid=Entry(window, bg='white', fg='black', bd=1, font='Cambria', textvariable=varstaffid)
staffid.place(x=200, y=200)


varperiod = StringVar()
label_b=Label(window, text='Hour', font="Cambria")
label_b.place(x=550, y=199)
period=Entry(window, bg='white', fg='black', bd=1, font='Cambria', textvariable=varperiod)
period.place(x=655, y=200)


varabsent = StringVar()
label_c=Label(window, text='Absentees', font="Cambria")
label_c.place(x=100, y=349)
absent=Entry(window, bg='white', fg='black', bd=1, font='Cambria', textvariable=varabsent)
absent.place(x=200, y=350)


varleave = StringVar()
label_c=Label(window, text='Duty Leave', font="Cambria")
label_c.place(x=550, y=349)
leave=Entry(window, bg='white', fg='black', bd=1, font='Cambria', textvariable=varleave)
leave.place(x=655, y=350)


capture=Button(window, text="Capture", font="Cambria", bd=0, activebackground="#2770f1", bg="#27e9f1", command=mkat)
capture.place(x=870, y=420)

#window creation and initialization

window.config(menu = menubar)
window.title('R.O.I')
window.geometry("984x666")
window.mainloop()