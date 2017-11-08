#!/usr/bin/python3
import time, datetime

# Calculate the product of the first 100,000 numbers.
def calcProd():
    product = 1
    for i in range(1, 100000):
        product *= i
    return product
startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % len(str(prod)))
time.sleep(1)                                       # pause program for 1 second
print('Took %s seconds to calculate.' % (endTime - startTime))

# datetime:
print("Computer's clock time: " + str(datetime.datetime.now()))
dt = datetime.datetime(2015, 10, 21, 16, 29, 0)     # year, month, day, hour, minute, second
print("dt's object years: %s, mon: %s, days: %s, hours: %s, min: %s, and sec: %s" % (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second))

now = datetime.datetime.fromtimestamp(time.time())
print('This moment(by Unix epoch): %s' % (now))     # returns a datetime obj for the moment n moments after the Unix epoch (got by time.time())

delta = datetime.timedelta(days = 11, hours = 10, minutes = 9, seconds = 8)     # represent a duration of time rather than a moment in time
print("Delta obj's duration: %s days, %s sec, %s microsec" % (delta.days, delta.seconds, delta.microseconds))
print('Total delta obj duration in seconds: %s' % (delta.total_seconds()))

thousandDays = datetime.timedelta(days = 1000)
print('Thousand days from now: ' + str(now + thousandDays))                     # calculate the date 1000 days from now
print((now < now + thousandDays))                   # datetime objs can be compared with each other and arithmetic operators can be used

# Printing datetime objects:
# strftime(format)                                  - returns string of time represented by the datetime obj, parsed using format string arg
# strptime(time_string, format)                     - returns a datetime obj of the time_string moment, parsed using format string arg
