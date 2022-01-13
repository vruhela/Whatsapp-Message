import pywhatkit

mobile = str(input('Enter Mobile No of Receiver with country code : '))
message = str(input('Enter Message you wanna send : '))
hour = int(input('Enter hour in 24 hour format : '))
minute = int(input('Enter minute in 24 hour format : '))

pywhatkit.sendwhatmsg(mobile,message,hour,minute)
