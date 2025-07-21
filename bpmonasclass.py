
'''blood pressure monitor refactored as series of functions rather than a class, which was overkill...'''
#class BP:
    #def __init__ (self,systol,diastol,pulse,weight):    
#        self.systol=systol
#        self.diastol=diastol
#        self.pulse=pulse
#        self.weight=weight
        #self.vitals=vitals
    #above are instance variables
    #def vitals(self):
    #    allvals='systolic{} diastolic {} pusle {} weight{}'(self.syst,self.dia,self.pulse,self.weight)
    #    return allvals 
    
def systol():
    '''systolic blood pressure reading'''
    try:
        syst=int(input('systolic bp?  '))
    except ValueError:
        print('Value must be an integer')
    return syst

def diastol():
    '''diastolic blood pressure reading'''
    try:
        dia=int(input('diastolic bp?  '))
    except ValueError:
        print('Value must be an integer')        
    return dia
    
def pulse_rate():
    '''pulse rate reading'''
    try:
    pulse=int(input('pulse rate?  '))
   except ValueError:
       print('Value must be an integer')
    return pulse

def weight():
    wt=int(input('your weight?  '))
    return wt

print (systol())
#readout=[systol(),diastol(),pulse_rate(),weight()]
#print (readout)

#-------------------------------------------------
#print('patient1 and patient2 objects in memory')
#patient1=BP(960,140,55,122)
#patient2=BP(60,40,55,1282)

#print("----------------------------------------------------------")
#print ('readout of patient1 and patient 2')
#print (patient1)
#print (patient2)

#print("----------------------------------------------------------")
#print('readout of patient2 systolic pressure')
#print (patient2.systol,patient2.diastol,patient2.pulse,patient2.weight)

#print ('p2 systol is',patient2.systol,'p2diastol is',patient2.diastol)
#print("----------------------------------------------------------")
#print('readout of patient1 weight')

#print (patient1.weight)
#print (f'systolic pressure is{patient1} and weight is {patient2}')

#print ('----------------------miscelanous--------------------------------')

#BP.systol()
