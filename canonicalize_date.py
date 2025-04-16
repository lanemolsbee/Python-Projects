def canonicalize_date(date_str):
    if "-"  in date_str:
        year = date_str[0:4]
        month = ""
        for i in range(5,7):
            if date_str[i] != "0":
                month += date_str[i]
        day = ""
        for i in range(8, 10):
            if date_str[i] != "0":
                day += date_str[i]
        return "{:d}-{:d}-{:d}".format(int(year), int(month), int(day))
    elif "/" in date_str:
        year = date_str[6:10]
        month = ""
        for i in range(0,2):
            if date_str[i] != "0":
                month += date_str[i]
        day = ""
        for i in range(3, 5):
            if date_str[i] != "0":
                day += date_str[i]
        return "{:d}-{:d}-{:d}".format(int(year), int(month), int(day))
    else:
        month = ""
        if date_str[0:3] == "Jan":
            month = "1"
        elif date_str[0:3] == "Feb":
            month = "2"
        elif date_str[0:3] == "Mar":
            month = "3"
        elif date_str[0:3] == "Apr":
            month = "4"
        elif date_str[0:3] == "May":
            month = "5"
        elif date_str[0:3] == "Jun":
            month = "6"
        elif date_str[0:3] == "Jul":
            month = "7"
        elif date_str[0:3] == "Aug":
            month = "8"
        elif date_str[0:3] == "Sep":
            month = "9"
        elif date_str[0:3] == "Oct":
            month = "10"
        elif date_str[0:3] == "Nov":
            month = "11"
        elif date_str[0:3] == "Dec":
            month = "12"
        day = ""
        year = ""
        if len(date_str) == 10:
            day = date_str[4]
            year = date_str[6:10]
        if len(date_str) == 11:
            day = date_str[5]
            year = date_str[7:11]
        return "{:d}-{:d}-{:d}".format(int(year), int(month), int(day))
        
