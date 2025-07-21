'''Convert to BP monitor with GUI'''
#keep simple==sys/dia/pulse/brief txt comment
import csv
import PySimpleGUI as sg


def save_contact(Time,Date,Systolic,Diastolic,Pulse,Weight):
    '''write data to csv file'''

    with open('BP_monitorGUI.csv', mode='a', newline='',encoding='UTF-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([Time,Date,Systolic ,Diastolic,Pulse,Weight,])

def get_contacts():
    '''review contacts'''
    contacts = []
    with open ('BP_monitorGUI.csv', mode='r',encoding='UTF-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            contacts.append(row)
    return contacts
         
def main():#date/syst/diast/pulse/short txt comment save to csv
    '''gui layout and logic'''
    sg.theme('SystemDefault')
    layout =[[sg.Text('Please enter rental information')],
    [sg.Text('Reading date', size =(15, 1)), sg.InputText(key='reading_date')],
    [sg.Text('Reading Time', size =(20, 1)), sg.InputText(key='reading_time')],
    [sg.Text('Systolic ', size =(15, 1)), sg.InputText(key='systolic')],
    [sg.Text('Diastolic', size =(20, 1)), sg.InputText(key='diastolic')],
    [sg.Text('Pulse', size =(20, 1)), sg.InputText(key='pulse')],
    [sg.Text('Weight',size=(20, 1)), sg.InputText(key='weight')],
    [sg.Save(), sg.Exit()]]

    window = sg.Window('Racquet Rental Tracker', layout)

    while True:
        event, values = window.read()
        if event == 'Save':
            save_contact(values['reading_date'],values['reading_time'],values['systolic'],
                         values['diastolic'],values['pulse'],values['weight']),
            sg.Popup('Reading Saved!')
        elif event == 'Exit':
            break
    window.close()

if __name__ == '__main__':
    main()

'''user input of blood pressure readings,weight and BMI
all misc prints/commented out stuff deleted. '''

#mport csv
#import os.path

#def custom_date():
#    '''user input--calendar date of bp reading to custom string'''
#    my_month=int(input('what month in mm format?  '))
#    my_day=int(input('what day  in dd format?  '))
#    my_year=int(input('what year in yy format?  '))
#    whole_date=f'{my_month}/{my_day}/{my_year}'
#    return whole_date

#weight=float(input('Give your weight in pounds. '))#make it global and be done. not a constant.

#def my_height():
#    '''user height input'''
#    height=int(input('Give your height in inches. '))
#    return height

#def BMI ():
#    '''bmi calculation'''
#    bmindex=(weight)/((my_height())**2)*703
#    return bmindex

#file_exists=os.path.isfile('BPMon3.csv')

#try:
#    Systolic=int(input('Systolic reading?  '))
#except ValueError:
#    print('input a NUMBER greater than 0')
#try:
#    Diastolic=int(input('Diastolic reading?  '))
#except ValueError:
#    print('input a NUMBER greater than 0')
#try:
#    Pulse=int(input('Pusle reading?  '))
#except ValueError:
#    print('input a NUMBER greater than 0')

#    
#file_exists=os.path.isfile('BPMon3.csv')#check if file exists
#    
#with open('BPMon3scratch.csv', 'a',newline='') as csvfile:
#    writerow=(['Date', 'Systolic', 'Diastolic','Pulse','Weight','BMI Calc'])
#    fieldnames = ['Date', 'Systolic','Diastolic','Pulse','Weight','BMI Calc']
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#        
#    if not file_exists:#if file does not exist generate column headers
#        writer.writeheader()

#    writer.writerow({'Date':custom_date(),'Systolic':Systolic,'Diastolic':Diastolic,\
#                                'Pulse':Pulse,'Weight':weight,'BMI Calc':BMI()})
#                                    
