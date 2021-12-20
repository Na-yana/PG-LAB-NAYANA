import datetime
t=datetime.time(22,56,44)
print(t)
print(t.hour)
print(t.second)
print(t.minute)



d=datetime.date.today()
print(d)
print(d.year)
print(d.month)


d1=datetime.date.today()
print(d1)
td=datetime.timedelta(days=2)
print (td)
d2=d1+td
print(d2)

dt=datetime.datetime.combine(d,t)
print(dt)


