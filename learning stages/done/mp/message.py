import pywhatkit as pwk
#send message to one person
pwk.sendwhatmsg("+91xxxxxxxxxx", "Hi, how are you?", 20, 34)
#send message to one person and close
pwk.sendwhatmsg("+91XXXXXX5980", "Hi", 18, 15, True, 5)
#send image to group with caption
pwk.sendwhats_image("Group_Name", "Media/image.png", "Hi")
#send image to group
pwk.sendwhats_image("Name", "Media/images.png")
#send message to group
pwk.sendwhatmsg_to_group("Group_Name", "Hey Guys! How's everybody?", 11, 0)
#instant message to group
pwk.sendwhatmsg_to_group_instantly("Group_Name", "Hey Guys Again!")