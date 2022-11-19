import sys
import cv2 
import face_recognition
import pickle
import pymongo
from tkinter import messagebox
from tkinter import *

#connecting to mongodb
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["attendance"]
mycol=mydb["student"]


window=Tk()
frame=Frame(window, borderwidth= 1, relief= 'groove', width=200, height=200)
frame.pack()
frame.place(x=100, y=200)

leftframe=Frame(window)
leftframe.pack(side= 'left')

label_s=Label(frame, text="Instructions", font="Cambria")
label_s.pack()
label_t=Label(frame, text= "Keep your head steady \n Ensure the surroundings are well lit \n A total of 3 photos will be taken \n Turn your head to opposite sides during 2nd and 3rd capture \n Ensure your face is captured proparly", font="Cambria")
label_t.pack(side='left')


varstudid = StringVar()
label_a=Label(window, text='Student ID', font="Cambria")
label_a.place(x=800, y=170)
studid=Entry(window, bg='white', fg='black', bd=0, font='Cambria', textvariable=varstudid)
studid.place(x=800, y=200)


varstudname = StringVar()
label_b=Label(window, text='Student Name', font="Cambria")
label_b.place(x=800, y=250)
studname=Entry(window, bg='white', fg='black', bd=0, font='Cambria', textvariable=varstudname)
studname.place(x=800, y=280)


varstudnumber = StringVar()
label_c=Label(window, text='Mobile No', font="Cambria")
label_c.place(x=800, y=320)
studnumber=Entry(window, bg='white', fg='black', bd=0, font='Cambria', textvariable=varstudnumber)
studnumber.place(x=800, y=350)


def reg():

    #adding a new student
    name=varstudname.get()
    ref_id=int(varstudid.get())
    phone=int(varstudnumber.get())
    studentlist=[{"_id":ref_id,"Name":name,"Phone":phone,"Status":"present"}]


    #creating a new file or opening the existing one
    try:
        f=open("ref_name.pkl","rb")

        ref_dictt=pickle.load(f)
        f.close()
    except:
        ref_dictt={}
    ref_dictt[ref_id]=name


    f=open("ref_name.pkl","wb")
    pickle.dump(ref_dictt,f)
    f.close()

    try:
        f=open("ref_embed.pkl","rb")

        embed_dictt=pickle.load(f)
        f.close()
    except:
        embed_dictt={}


    #capturing three different angles
    for i in range(3):
        key = cv2. waitKey(1)
        webcam = cv2.VideoCapture(0)
        while True:
       
            check, frame = webcam.read()

            cv2.imshow("Capturing", frame)
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]
  
            key = cv2.waitKey(1)

            if key == ord('s') : 
                face_locations = face_recognition.face_locations(rgb_small_frame)
                if face_locations != []:
                    face_encoding = face_recognition.face_encodings(frame)[0]
                    if ref_id in embed_dictt:
                        embed_dictt[ref_id]+=[face_encoding]
                    else:
                        embed_dictt[ref_id]=[face_encoding]
                    webcam.release()
                    cv2.waitKey(1)
                    cv2.destroyAllWindows()     
                    break
            elif key == ord('q'):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break
    

    #updating the file
    f=open("ref_embed.pkl","wb")
    pickle.dump(embed_dictt,f)
    f.close()

    #creating details in database#
    mycol.insert_many(studentlist)
    messagebox.showinfo("Done","New student created")

    studid.delete(0,END)
    studname.delete(0,END)
    studnumber.delete(0,END)


capture=Button(window, text="Capture", font="Cambria", bd=0, activebackground="#2770f1", bg="#27e9f1", command=reg)
capture.place(x=870, y=420)


window.title('R.O.I')
window.geometry("1084x666")
window.mainloop()