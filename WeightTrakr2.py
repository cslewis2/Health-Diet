def todays_run():
    """Run data for a given day."""
    run_dist=float(input('distance run?'))
    run_mins=int(input('time run in mins?'))
    avg_speed=float(input('speed run in mph?'))
    kcals=int(input('kcals burned?'))
    fat_cals=int(input('fat cals burned?'))
    return (run_dist,run_mins,avg_speed,kcals,fat_cals)
    
print(todays_run())
