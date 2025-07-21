class RunTrack:
    def __init__(self, run_dist,run_mins,avg_speed,kcals,fat_cals):
        """Create a new WizCoin object with galleons, sickles, and knuts."""
        #self.run_date-run_date
        self.run_dist = run_dist==float(input('distance run?  '))
        self.run_mins = run_mins==int(input('run time in mins?  '))
        self.avg_speed  = avg_speed=avg_speed==float(input('speed in mph?  '))
        self.kcals = kcals==int(input('kcals burned?  '))
        self.fat_cals = fat_cals==int(input('fat_cals burned?  '))
        # NOTE: __init__() methods NEVER have a return statement.
    
    def todays_run(self):
        """Run data for a given day."""
        run_dist=float(input('distance run?'))
        run_mins=int(input('time run in mins?'))
        avg_speed=float(input('speed run in mph?'))
        kcals=int(input('kcals burned?'))
        fat_cals=int(input('fat cals burned?'))
        return (run_dist,run_mins,avg_speed,kcals,fat_cals)
j=RunTrack().todays_run()
print(j)

    #def weightInGrams(self):
        #"""Returns the weight of the coins in grams."""
       # return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)
