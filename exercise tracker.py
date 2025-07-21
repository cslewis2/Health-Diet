
from datetime import date
import csv
import json
#distance traveled
#time run
#caloreis burned
#speed run

def workouts():
    wrkdat=date.today()
    tdistance= float(input('Distance run?  '))
    ttime=int(input('How long did you run (minutes) '))
    tspeed=float(input('How fast did you run (mph)? '))  
    tcalories=int(input('How many calories burned? '))
    return (wrkdat,tdistance,ttime,tspeed,tcalories)
print (workouts())
datum=[]
datum.append[workouts()]
print (datum)

#fieldnames=['run-distance','run-time','run-speed','cals-burn']
##print (jsondumps dstance,ttime,tspeed,tcalories,tfactals)

#with open('ExerciseTracker.csv', 'a', newline='') as csvfile:
##function open ('filename.CSV),r-read,w-write-a-append (add to) as filetype csvfile:
##use with because it implicitly calls a file close for the file when done
#       fieldnames=['run-distance','run-time','run-speed','cals-burn']

##fieldnames function defines ROW 1 in spreadsheet, column headers in single quotes in form of a list
#        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
##dictwriter is a dictionary utility function for python created csv files...transcribes a python dictionary to csv file
#        writer.writeheader()
##if this line not included, will take first line of data as ROW 1...is optional with dictwriter but required otherwise
#        for a in range (0,total_guests):
#                writer.writerow({'WrkDate':),'distance':),\
#                'Guest_Address':guest_address(),'Member_Name':member_name()\
#                })


##with open('ExerciseTracker.csv', 'a', newline='') as csvfile:
###function open ('filename.CSV),r-read,w-write-a-append (add to) as filetype csvfile:
###use with because it implicitly calls a file close for the file when done
##        fieldnames = ['Date','Guest_Name','Guest_Address','Member_Name']
###fieldnames function defines ROW 1 in spreadsheet, column headers in single quotes in form of a list
##        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
##dictwriter is a dictionary utility function for python created csv files...transcribes a python dictionary to csv file
#        writer.writeheader()
##if this line not included, will take first line of data as ROW 1...is optional with dictwriter but required otherwise
#        for a in range (0,total_guests):
#                writer.writerow({'Visit_Date':visit_date(),'Guest_Name':guest_name(),\
#                'Guest_Address':guest_address(),'Member_Name':member_name()\
#                })