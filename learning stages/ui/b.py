import sys
import cv2 
import face_recognition
import pickle
from tkinter import *

window=Tk()

label_a=Label(window, text='Student ID', font="Cambria")
label_a.place(x=900, y=170)
studid=Entry(window, bg='white', fg='black', bd=0, font='Cambria')
studid.place(x=900, y=200)


label_b=Label(window, text='Student Name', font="Cambria")
label_b.place(x=900, y=250)
studname=Entry(window, bg='white', fg='black', bd=0, font='Cambria')
studname.place(x=900, y=280)


capture=Button(window, text="Capture", font="Cambria", bd=0, activebackground="#2770f1", bg="#27e9f1")
capture.place(x=970, y=350)

window.title('Register New Student')
window.geometry("1184x666")
window.mainloop()