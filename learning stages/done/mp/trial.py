#importing pywhatkit
import pywhatkit as pwk

#importing pymongo
import pymongo

#connecting to mongodb
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["exam"]
mycol=mydb["student"]


cun="+91"
#fetching details from mongodb
student=mycol.find({"Department":"MCA"})
for i in student:
    num=str(i["Phone"])
    mob=cun+num
    #send message to one person
    pwk.sendwhatmsg_instantly(mob, "Hi, how are you?")
    print("message sent to "+i["Name"]+" "+mob)

    