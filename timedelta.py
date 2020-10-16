#get datetime after 5 days
from datetime import datetime, timedelta
dt = datetime(2020,10,16,11,22,50)

add_dt = dt + timedelta(days=5)

print(add_dt)



