import csv
from datetime import date

#def BMI ():
#    weight=int(input('what is your weight in pounds'))
#    height=int(input('what is your height in inches'))   
#    #lb_kg=(weight)/2.2)
#    #in_cm=(height)*2.54)
#    bmindex=((weight)/((height)**2)*703)
#    return bmindex
#print (BMI())\
#printing for error checks
#{'Date':date.today(),'systolic':number,'diastolic':number,'pulse':number}
#reads=int(input('how many readings are you taking?'))
#for readings in range (0,reads):
#finread=[]
reads=int(input('how many readings are you taking?'))
for readings in range (0,reads): # will ask for readings even though want 1...data_reads=reads..maybe do library in loop?
    def pressure():
        systolic= int(input('systolic reading?  '))
        diastolic= int(input('diastolic reading?  '))
        #rds=[]
        #rds.append(syst)
        return systolic,diastolic       
    #for final in range (0,reads):
    finread=[]
    finread.append(pressure())
    print (finread)

    writerow=(['A1', 'B1', 'C1',''])
#that library should be specifically on first row as header (optional)
    project_titles = (['Date', 'pressure(?)'])
#variable containing data, in this case 3 strings
    with open('BPMonitor.csv', 'a') as f:
#opens given 'filename' and writes 'w' as a file 'f:'
        csv.writer(f).writerow((pressure())) #NO this is calling function again and giving every even answer
#writes variable 'project_titles' in individual cells of csv file
#ie 1 item per cell

#initiate excel file...
##csvwriter f: ('bptry.csv',a),blahblahblah

