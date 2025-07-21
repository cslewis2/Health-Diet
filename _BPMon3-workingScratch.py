'''user input of blood pressure readings,weight and BMI
all misc prints/commented out stuff deleted. '''

import csv
import os.path

def custom_date():
    '''user input--calendar date of bp reading to custom string'''
    my_month=int(input('what month in mm format?  '))
    my_day=int(input('what day  in dd format?  '))
    my_year=int(input('what year in yy format?  '))
    whole_date=f'{my_month}/{my_day}/{my_year}'
    return whole_date

weight=float(input('Give your weight in pounds. '))#make it global and be done. not a constant.

def my_height():
    '''user height input'''
    height=int(input('Give your height in inches. '))
    return height

def BMI ():
    '''bmi calculation'''
    bmindex=(weight)/((my_height())**2)*703
    return bmindex

file_exists=os.path.isfile('BPMon3.csv')

try:
    Systolic=int(input('Systolic reading?  '))
except ValueError:
    print('input a NUMBER greater than 0')
try:
    Diastolic=int(input('Diastolic reading?  '))
except ValueError:
    print('input a NUMBER greater than 0')
try:
    Pulse=int(input('Pusle reading?  '))
except ValueError:
    print('input a NUMBER greater than 0')

    
file_exists=os.path.isfile('BPMon3.csv')#check if file exists
    
with open('BPMon3scratch.csv', 'a',newline='') as csvfile:
    writerow=(['Date', 'Systolic', 'Diastolic','Pulse','Weight','BMI Calc'])
    fieldnames = ['Date', 'Systolic','Diastolic','Pulse','Weight','BMI Calc']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
    if not file_exists:#if file does not exist generate column headers
        writer.writeheader()

    writer.writerow({'Date':custom_date(),'Systolic':Systolic,'Diastolic':Diastolic,\
                                'Pulse':Pulse,'Weight':weight,'BMI Calc':BMI()})
                                    
