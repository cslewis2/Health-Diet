'''user input of blood pressure readings,weight and BMI'''

import csv
import os.path

def custom_date():
    '''calendar date of reading entry by user custom string'''
    my_month=int(input('what month in mm format?  '))
    my_day=int(input('what day  in dd format?  '))
    my_year=int(input('what year in yy format?  '))
    whole_date=f'{my_month}/{my_day}/{my_year}'
    return whole_date

weight=float(input('Give your weight in pounds. '))#make it global and be done. not a constant.
# def my_weight():
#     '''user weight input'''
#     weight=float(input('Give your weight in pounds. '))
#     BMI_weight=weight*1
#     # if weight <=0:
#     #     print ('weight less than zero')
#     #     return None
#     return weight,BMI_weight

# print(my_weight)
# final_weights=my_weight

def my_height():
    '''user height input'''
    height=int(input('Give your height in inches. '))
    # if height <=0:
    #     # print ('height less than zero')
    #     return None
    return height


def BMI ():
    '''bmi calculation'''
    
    # height=int(input('what is your height in inches?  '))
    # default_height_inches=70
    # if height<=0:
        # print (f'returning default height of {default_height_inches} inches')
    # return default_height_inches
    
    #lb_to_kg=(weight)/2.2)
    #in_to_cm=(height)*2.54)
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
    
file_exists=os.path.isfile('BPMon3.csv')
    
with open('BPMon3.csv', 'a',newline='') as csvfile:
    writerow=(['Date', 'Systolic', 'Diastolic','Pulse','Weight','BMI Calc'])
    fieldnames = ['Date', 'Systolic','Diastolic','Pulse','Weight','BMI Calc']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
    if not file_exists:
        writer.writeheader()

    writer.writerow({'Date':custom_date(),'Systolic':Systolic,'Diastolic':Diastolic,\
                                'Pulse':Pulse,'Weight':weight,'BMI Calc':BMI()})
                                    
