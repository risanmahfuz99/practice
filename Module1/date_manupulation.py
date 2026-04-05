import datetime
from datetime import timedelta
from dateutil import tz

print(datetime.datetime.now())

print (datetime.datetime.now()+timedelta(days=2)) # add or subtract time from a certion date





tz_string = datetime.datetime.now(datetime.timezone.utc).astimezone().tzname()

print("datetime.now() :", tz_string)

NYC = tz.gettz('Europe / Berlin')
datetime1 = datetime.datetime(2015, 5, 21, 12, 0)
datetime2 = datetime.datetime(2015, 12, 21, 12, 0, tzinfo = NYC)

print("Naive Object :", datetime1.tzname())
print("Aware Object :", datetime2.tzname())