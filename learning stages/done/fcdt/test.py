import cv2
import face_recognition
import cv2
import sys

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
 
imgdon = face_recognition.load_image_file('don.jpg')
imgdon = cv2.cvtColor(imgdon,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('img2.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)
 
faceLoc = face_recognition.face_locations(imgdon)[0]
encodedon = face_recognition.face_encodings(imgdon)[0]
cv2.rectangle(imgdon,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)
 
faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)
 
results = face_recognition.compare_faces([encodedon],encodeTest)
faceDis = face_recognition.face_distance([encodedon],encodeTest)
print(results,faceDis)
cv2.putText(imgTest,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
 
cv2.imshow('Don',imgdon)
cv2.imshow('Testing image',imgTest)
cv2.waitKey(0)
