#import my_module as mm #short form mm supported in python
from my_module import find_index , test
import sys
import random #to provide random values
import datetime #to provide a date
import calendar #to get the year information
import math #to do mathematical operation
import os
import antigravity


course=["History","Math", "physics","compsci"]
index= find_index(course, "compsci")
print(index)
print(test)
 

# print(sys.path)  to know the path


#Random Library
rc = random.choice(course)
print(rc)

#for mathematics
rads = math.radians(90)
print(rads)

#for datetime
t = datetime.date.today()
print(t)

#for calender
print(calendar.isleap(2020))

#to check the current working directry
print(os.getcwd())