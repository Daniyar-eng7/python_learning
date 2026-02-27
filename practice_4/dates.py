#1
from datetime import datetime, timedelta

now=datetime.now()
five=now-timedelta(days=5)
print(five)


#2
from datetime import datetime, timedelta

now= datetime.now()
print(now-timedelta(days=1))
print(now)
print(now+ timedelta(days=1))



#3
from datetime import datetime, timedelta

now= datetime.now()
print(now.strftime("%Y-%m- %d, %H:%M:%S"))


#4
from datetime import datetime, timedelta

birthday=input()
dt=datetime.strptime(birthday, "%Y-%m-%d %H:%M:%S")

now=datetime.now()
print(dt-now)