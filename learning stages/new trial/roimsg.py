#importing pywhatkit
import pywhatkit as pwk

#importing pymongo
import pymongo

#connecting to mongodb
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["attendance"]
mycol=mydb["student"]


cun="+91"
#fetching details from mongodb
student=mycol.find({"Status":"absent"})
for i in student:
    num=str(i["Phone"])
    mob=cun+num
    #send message to one person
    msg="Your Child "+i["Name"]+" is absent in class"
    pwk.sendwhatmsg_instantly(mob, msg)
    print("message sent to "+i["Name"]+"'s parent")

    