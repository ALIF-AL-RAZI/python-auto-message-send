import pywhatkit

for x in range(4): #automatically send 4 messages
    #pywhatkit.sendwhatmsg("'''The mobile number where you want send meassages. example: '''0123456789", 'hi', 19, 33)  #in sendwhatmsg() 19 is hour and 33 is minutes. that means in 19:33 it will send meassage
    pywhatkit.sendwhatmsg_instantly("'''The mobile number where you want send meassages. example: '''0123456789",'hi', 7, True,2) # Here it will send messages instantly after running codes. true is used close the tab which was opened automatically after runnning code.



