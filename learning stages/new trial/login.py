from tkinter import *

window=Tk()

menubar=Menu(window)

attendance = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Attendance', menu = attendance)
attendance.add_command(label = 'Take Attendance', command = None)
attendance.add_command(label = 'View Attendance', command = None)

alert = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Alert', menu = alert)
alert.add_command(label = 'Send Alert', command = None)

help = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Help', menu = help)
help.add_command(label = 'Get Help', command = None)
help.add_separator()
help.add_command(label = 'About ROI', command = None)


window.config(menu = menubar)
window.title('R.O.I')
window.geometry("1184x666")
window.mainloop()