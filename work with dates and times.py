import datetime
import pytz
date = datetime.datetime.now()
date_today = datetime.datetime.today()
date_utc = datetime.datetime.utcnow()
print('Here the all different time zones',date,date_today,date_utc)
print(date)
date_in_string = date.strftime("%d/%m/%Y %H:%M:%S")
print(date_in_string)
date_inutc = date.utcnow()
print(date_inutc)
time_stamp = date.timestamp()
print(time_stamp)
time_stamp_in_string = datetime.datetime.fromtimestamp(time_stamp)
print(time_stamp_in_string)
print(date.year)
print(date.day)
print(date.timestamp())
print(date.month)

# Use of PYTZ

#
dt = datetime.datetime.now(pytz.timezone('Asia/Karachi'))
print(dt)


for tz in pytz.all_timezones:
    print(tz)