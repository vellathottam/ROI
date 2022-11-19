import face_recognition
import cv2
import numpy as np
import glob
import pickle
import pymongo 

#loading pickle files
f=open("ref_name.pkl","rb")
ref_dictt=pickle.load(f)        
f.close()

f=open("ref_embed.pkl","rb")
embed_dictt=pickle.load(f)      
f.close()


#lists to store name and embeddings
known_face_encodings = []  
known_face_names = []  


for ref_id , embed_list in embed_dictt.items():
    for my_embed in embed_list:
        known_face_encodings +=[my_embed]
        known_face_names += [ref_id]


#capturing video with webcam
video_capture = cv2.VideoCapture(0)

face_locations = []
face_encodings = []
p_names = set()
face_names = []
process_this_frame = True

while True  :
  
    ret, frame = video_capture.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:

            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            face_names.append(name)
            p_names.add(name)

    process_this_frame = not process_this_frame

    for (top_s, right, bottom, left), name in zip(face_locations, face_names):
        top_s *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top_s), (right, bottom), (0, 255, 0), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, ref_dictt[name], (left + 6, bottom - 6), font, 1.0, (0, 0, 255), 1)
        font = cv2.FONT_HERSHEY_DUPLEX

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()


#preparing attendance list to update database
attendance_list = []


for present in p_names:
    attendance_list.append(present)


#selecting and printing details of absent students
absent_list = list(ref_dictt.keys())

for s_id in attendance_list:
    absent_list.remove(s_id)

print("list of absent students")
for s_id in absent_list:
    print(s_id)


#collecting data of students with duty leave
exp_stu_id=input("Enter the Student ID of students to be given exception")
dutyleave=list(map(str,exp_stu_id.split()))


#updating attendance list to include students with duty leave
for s_id in dutyleave:
    attendance_list.append(s_id)
    absent_list.remove(s_id)




#connecting to mongodb
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["attendance"]
mycol=mydb["student"]


#marking attendance in DB
for s_id in attendance_list:
    st_id = int(s_id)
    mycol.update_many({"_id":st_id},{"$set" :{"Status":"present"}})

for s_id in absent_list:
    st_id = int(s_id)
    mycol.update_many({"_id":st_id},{"$set" :{"Status":"absent"}})


print("Done")