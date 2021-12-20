import time
print(time.time())
print(time.ctime())
print(time.ctime(time.time()+30))

t=time.localtime()
print(t)
print(t.tm_year)
print(t.tm_mday)
print(t.tm_hour)
print(t.tm_wday)
print(t.tm_yday)
print(t.tm_mon)



import calender
