def add_time(start, duration, day = ""):
    #split out data
    x = start.split()
    y = x[0].split(":")   
    z = duration.split(":")
    
    AMorPM = x[1]
    start_h = int(y[0])
    start_m = int(y[1])
    dur_h = int(z[0])
    dur_m = int(z[1])


    newAMorPM = AMorPM
    newday = day
    carry_h = 0
    carry_d = 0

    #calculate new minute
    new_m = start_m + dur_m
    if new_m >= 60:
        new_m -= 60
        carry_h = 1

    #calculate new hour
    new_h = start_h + dur_h + carry_h
    carry_d = int(new_h / 24)
    new_h = new_h % 24
    if new_h >= 12:
        
        if AMorPM == "AM":
            newAMorPM = "PM"
        else:
            newAMorPM = "AM"
            carry_d += 1
        if new_h > 12:
            new_h -= 12 

    #calculate days later
    #If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.
    if carry_d > 0:
        if carry_d == 1:
            dayslater = " (next day)"
        else:
            dayslater = " (" + str(carry_d) + " days later)"
    else:
        dayslater = ""
        
    days = { 1 : "Monday", 2 : "Tuesday", 3 : "Wednesday", 4 : "Thursday", 5 : "Friday" , 6 : "Saturday", 7 : "Sunday" }
    #calculate day
    if day != "":
        day = (day.lower()).capitalize()
        for key in days:
            if days[key] == day:
                daykey = key
                break
        daykey += carry_d
        if daykey > 7:
            daykey = daykey % 7
        newday = ", " + days[daykey]
        
    new_time= str(new_h) + ":" + (str(new_m)).zfill(2) + " " + newAMorPM + newday + dayslater

    return new_time