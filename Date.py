#membuat Current Time dan Date

import datetime
now = datetime.datetime.now()
print ("Tanggal dan Jam:  ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#Current date and time using strftime:
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#Current date with another version:
import datetime
now = datetime.datetime.now()
print ("Current date and time: ")
time_now = (now.year,now.month,now.day,now.hour,now.minute,now.second)
print (time_now)

import datetime
now = datetime.datetime.now()
print ("Current date and time for Year: ")
print (now.strftime("%Y"))
print (now.strftime("%m"))
print (now.strftime("%d"))