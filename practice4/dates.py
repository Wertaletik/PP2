import datetime

now = datetime.datetime.now()
daysago5 = now - datetime.timedelta(days=5)
print(daysago5)




print("-"*100)
yesterday = now - datetime.timedelta(days=1)
tomorrow = now + datetime.timedelta(days=1)
print(yesterday.date())
print(now.date())
print(tomorrow.date())




print("-"*100)
nomicro = now.replace(microsecond=0)
print(nomicro)




print("-"*100)
date1=datetime.datetime(2026,12,31,23,59,53)
date2=datetime.datetime(2026,12,31,23,59,32)
print(abs((date2-date1).total_seconds()))