import csv
from collections import namedtuple
from random import randint
from datetime import date


walker=namedtuple('walker',['date','distance','time','speed','calburn','weight'])

walker.date=date.today()

try:
    walker.distance=float(input('distance run? '))
except ValueError: 
    print('use numbers only')

try:
    walker.time=float(input('time run? '))
except ValueError:
    print('use numbers only')
    
try:
    walker.speed=float(input('speed run? '))
except ValueError:
    print('use numbers only')

try:
    walker.calburn=float(input('cals burned? '))
except ValueError:
    print('use numbers only')

try:
    walker.weight=float(input('weight today? '))
except ValueError:
    print('use numbers only')

print ([walker.date,walker.distance,walker.time,walker.speed,walker.calburn])
print (date.today())
print (walker)

with open ('TRKR.csv','a',newline='') as csvfile:
        fieldnames = ['dat_work','time_minutes','distance_miles',
                     'speed_mph','Calories','weight_lbs']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'dat_work':walker.date,'time_minutes':walker.time,
                        'distance_miles':walker.distance,'speed_mph':walker.speed,
                        'Calories':walker.calburn,'weight_lbs':walker.weight})

print('-----------------------------------------------------')

