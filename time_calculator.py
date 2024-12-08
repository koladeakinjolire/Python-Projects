def add_time(start, duration, day=None):
  weekdays_index = {'monday':0, 'tuesday':1,'wednesday':2,'thursday':3,'friday':4,'saturday':5,'sunday':6}
  weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
  start_time, start_period = start.split()
  start_hour, start_minute = map(int, start_time.split(":"))
  duration_hour, duration_minute = map(int, duration.split(":"))
  period_change = {"AM" : "PM", "PM":"AM"}
  days_later = int(duration_hour / 24)
  end_minute = start_minute + duration_minute
  if end_minute >= 60:
    start_hour += 1
    end_minute = end_minute % 60
  
  period_flip = int((start_hour + duration_hour) / 12)
  end_hour = (start_hour + duration_hour) % 12
  end_minute = end_minute if end_minute > 9 else '0' + str(end_minute)
  end_hour = end_hour = 12 if end_hour == 0 else end_hour
  if start_period == 'PM' and start_hour + (duration_hour % 12) >= 12:
    days_later += 1
  
  start_period = period_change[start_period] if period_flip % 2 == 1 else start_period
  end_time = str(end_hour) + ":" + str(end_minute) + " " + start_period
  if day:
    day = day.lower()
    index = int((weekdays_index[day]) + days_later) % 7
    new_day = weekdays[index]
    end_time += ', ' + new_day

  if days_later == 1:
    end_time +=  " " + "(next day)"
  elif days_later > 1:
    end_time += f' ({days_later} days later)'
  
  return end_time


print(add_time('4:05 PM', '5:04'))
print(add_time('2:59 AM', '24:00'))
print(add_time('5:16 AM', '6:04'))
print(add_time('6:25 PM', '7:06'))
print(add_time('7:36 AM', '16:04'))
print(add_time('8:45 PM', '13:04'))
print(add_time('9:58 AM', '16:08'))
print(add_time('10:09 PM', '5:04', 'Monday'))
print(add_time('6:15 AM', '5:04', 'Tuesday'))
print(add_time('4:05 PM', '234:44'))
print(add_time('5:06 AM', '456:04'))



