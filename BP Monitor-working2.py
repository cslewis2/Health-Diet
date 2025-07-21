import csv
import os.path
from datetime import date,datetime

def BMI ():
    weight=int(input('your weight in pounds? Enter 0 if no reading. BMI will be 0'))
    
    height=int(input('what is your height in inches? if csl enter zero--auto 70 inches'  ))
    if height<=0:
        print ('if not csl input your height in inches...')
        height=70
    #if height>0:
        #continue
        #height=HEIGHT=70 #inches
    
    #lb_kg=(weight)/2.2)
    #in_cm=(height)*2.54)
    bmindex=((weight)/((height)**2)*703)
    return weight,bmindex

#above function works just fine

#print (BMI()) 
#with open('BPMonitor.csv', 'a',newline='') as csvfile:
#        writerow=(['Date', 'Systolic', 'Diastolic','Pulse','BMI Calc'])
#fieldnames = ['Date', 'Systolic','Diastolic','Pulse','BMI Calc']

bp_readings=int(input('how many measurements?  '))

file_exists=os.path.isfile('BPMon.csv')


for i in range(bp_readings):
    
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
        
        #if Systolic <=0 or Diastolic <=0 or Pulse<=0:
         #   print('The dead live!!! Try whole number greater than zero')
        #continue
        #break
    
    file_exists=os.path.isfile('BPMon.csv')
    
    with open('BPMon.csv', 'a',newline='') as csvfile:
        writerow=(['Date', 'Systolic', 'Diastolic','Pulse','BMI Calc'])
        fieldnames = ['Date', 'Systolic','Diastolic','Pulse','BMI Calc']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()

        writer.writerow({'Date':date.today(),'Systolic':Systolic,'Diastolic':Diastolic,\
                                    'Pulse':Pulse,'BMI Calc':BMI()})
                                    
