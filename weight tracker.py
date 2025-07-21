
import csv
from datetime import date
from collections import namedtuple

'''A simple exercise log for personal use'''
#find a way to redo from start if value error triggered...break statement with logic???

#continue,break,stop,halt,redofromstart,

run_day=date.today()
try:
    run_time=float(input('how long was the run in minutes?  '))
except ValueError:
        print('time value must be a positive number in minutes')

try:
    distance=float(input('distance covered in miles? '))
except ValueError:
    print('distance value must be a positive number')
    
try:
    speed=float(input('treadmill speed in mph?  '))
except ValueError:
    print('speed must be a positive number')

try:
    Cals_burn=float(input('how many Calories burned?  '))
except ValueError:
    print('Calories can only be positive number')

with open('ExerciseTracking.csv', 'a', newline='') as csvfile:
        fieldnames = ['dat_work','time_minutes','distance_miles',
                     'speed_mph','Calories']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'dat_work':run_day,'time_minutes':run_time,'distance_miles':distance,'speed_mph':speed,'Calories':Cals_burn})

namedtuple('runlog',date.today(),time,distance,speed,Calories)