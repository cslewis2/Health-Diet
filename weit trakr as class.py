class RunTrack:
    def __init__(self, run_dist,run_mins,avg_speed,kcals,fat_cals):
        """Create a new WizCoin object with galleons, sickles, and knuts."""
        #self.run_date-run_date
        self.run_dist = run_dist
        self.run_mins = run_mins
        self.avg_speed  = avg_speed
        self.kcals = kcals
        self.fat_cals = fat_cals
        # NOTE: __init__() methods NEVER have a return statement.

    def value(self):
        """The value (in knuts) of all the coins in this WizCoin object."""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    def weightInGrams(self):
        """Returns the weight of the coins in grams."""
        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)
