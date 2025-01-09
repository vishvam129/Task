# How can you handle Timezones in python? Make one Example of it.
import datetime
import pytz
dtObject_utc = datetime.datetime.now(pytz.utc) 
date_africa = datetime.datetime.now(pytz.timezone('Africa/Abidjan'))
date_america = datetime.datetime.now(pytz.timezone('America/Toronto'))
print(f"timezone of africa is {date_africa}")
print(f"timezone of america is {date_america}")
# convert timezone

date_asia=date_america.astimezone(pytz.timezone('Indian/Chagos'))
print(f"The converted timezone is {date_asia}")