class Date:
    '''
    This class represents dates.
    Primary methods: init, str
    Construction: a date string and an
    initial event string associated with that date

    '''
    def __init__(self, date, event):
        '''
        This is the constructor method for Date objects.
        Parameters:
        date is a string representing a date
        event is a string representing an event that
        occurred on the particular date supplied
        Returns:
        nothing
        '''        
        self._date  = date
        self._event = [event]
        
    def get_date(self):
        '''
        This function accesses the date variable.
        Parameters: none (excluding self)
        Returns:
        the value of the date object variable
        '''
        return self._date
    
    def get_event(self):
        '''
        This function accesses the event variable.
        Parameters: none (excluding self)
        Returns:
        the value of the event object variable
        '''
        return self._event
    def add_event(self, event):
        '''
        This function adds an event to the event list.
        Parameters:
        event is a string to be added to the list of events
        that occurred on that date.
        Returns: nothing
        '''
        self._event.append(event)

    def __str__(self):
        '''
        This function converts the Date object to a string.
        Arguments: none (excluding self)
        Returns: a string representation of the Date object
        '''
        # Create the initial date string
        date_string = ""
        self._event = sorted(self._event)
        # Concatenate each individual event
        for i in range(len(self._event) - 1):
            date_string += self._date + ": "
            date_string += self._event[i]
            date_string += "\n"
        # Concatenate the last event or only event
        date_string += self._date + ": "
        date_string += self._event[len(self._event) - 1]
        
        return date_string
        
class DateSet:
    '''
    This class represents a collection of dates
    as well as the events associate with those dates
    Primary methods: init, str
    Construction: no parameters, creates
    an initially empty dictionary as an object variable
    to store the dates and events
    This class does all the work of putting dates
    in canonical form as well as storing Date objects.
    '''
    def __init__(self):
        '''
        Constructor for the DateSet class. 
        Parameters: none (excluding self)
        Returns: nothing (it is a constructor)
        '''
        self._dates = {}

    def add_date(self, date, event):
        '''
        This function adds a new date object to
        the dictionary, or adds an event to an
        already existing date and its list of events.
        Parameters:
        date is a string representing a date
        event is a string representing an event that
        occurred on that date. 
        '''
        # Canonicalize the date
        date = self.canonicalize_date(date)
        if date not in self._dates:
            self._dates[date] = Date(date, event)
        else:
            self._dates[date].add_event(event)
    def __str__(self):
        '''
        This function creates a string representation
        of an object of the DateSet class.
        Parameters: none (exluding self)
        Returns: a string representation of 
        an object of this class. 
        '''
        all_items = ""
        # Add on the string represention of each Date object
        for item in self._dates.values():
            all_items += str(item)
        return all_items
    def get_dict(self):
        '''
        This function gets the dictionary of Date objects
        Parameters: none (excluding self)
        Returns:
        the dictionary of Date objects
        '''
        return self._dates
    def canonicalize_date(self, date):
        '''
        This function canonicalizes the date.
        Parameters: date is a string representing
        the date to be canonicalized
        Returns:

        '''
        date = date.strip()
        year = ""
        month = ""
        day = ""
        canonicalized = ""
        # Canonicalize dates in the form yyyy-mm-dd
        if "-"  in date:
            year = date[0:4]
            # Adjust for whether there are leading
            # zeros in any part of the date in both ifs.
            if len(date) == 10:
                month = date[6]
                day = date[8:10]
            
            elif len(date) == 9:
                month = date[5]
                day = date[7:9]

            # Format the values into the canonical date.
            canonicalized = "{:d}-{:d}-{:d}".format(int(year)
            , int(month), int(day))
        # Canonicalize dates in the form mm/dd/yyyy
        elif "/" in date:
            year = ""
            month = ""
            day = ""
            # Adjust for leading zeros in parts of the date
            # for all three if statements
            if len(date) == 8:
                year = date[4:8]
                month = date[0]
                day = date[2]
            
            elif len(date) == 9:
                year = date[5:9]
                month = date[0]
                if date[2] != "0":
                    day += date[2]
                day += date[3]
                    
            elif len(date) == 10:
                year = date[6:10]
                month = date[1]
                day = ""
                if date[3] != "0":
                    day += date[3]
                day += date[4]
                    
            
            canonicalized = "{:d}-{:d}-{:d}".format(int(year),
             int(month), int(day))
        # Canonicalize the dates in the form Month day year
        else:
            month = ""
            if date[0:3] == "Jan":
                month = "1"
            elif date[0:3] == "Feb":
                month = "2"
            elif date[0:3] == "Mar":
                month = "3"
            elif date[0:3] == "Apr":
                month = "4"
            elif date[0:3] == "May":
                month = "5"
            elif date[0:3] == "Jun":
                month = "6"
            elif date[0:3] == "Jul":
                month = "7"
            elif date[0:3] == "Aug":
                month = "8"
            elif date[0:3] == "Sep":
                month = "9"
            elif date[0:3] == "Oct":
                month = "10"
            elif date[0:3] == "Nov":
                month = "11"
            elif date[0:3] == "Dec":
                month = "12"
            day = ""
            year = ""
            # Account for leading zeros
            if len(date) == 10:
                day = date[4]
                year = date[6:10]
            if len(date) == 11:
                day = date[4:6]
                year = date[7:11]
            canonicalized = "{:d}-{:d}-{:d}".format(int(year),
             int(month), int(day))
        date = canonicalized
        return date
    def search_date(self, date):
        '''
        This function searches the DateSet's
        dictionary instance variable and prints
        out the events associated with a specific date
        that is converted to canonicalized form. 
        Parameters:
        date is a string representing a date
        Returns: nothing
        '''
        date = self.canonicalize_date(date)
        for date_key in self._dates:
            if date == date_key:
                print(self._dates[date])


def main():
    '''
    This function serves to test the Date
    and DateSet classes.
    Parameters: none
    Returns: nothing
    '''
    file_name = input()
    file = open(file_name, "r")
    items = DateSet()
    for line in file:
        # If the line contains the I operation,
        # add a date or event to the DateSet object.
        if line[0] == "I":
            line = line[2:].split(":")
            for i2 in range(len(line)):
                line[i2] = line[i2].strip()
            # Join together everything after date
            content = ":".join(line[1:]) 
            
            items.add_date(line[0], content)
        # Otherwise, print all events associated
        # with the provided date.
        elif line[0] == "R":
            line = line[2:]
            
            items.search_date(line)                     
            
        # If neither was true, print an error message.
        elif line[0] != "I" and line[0] != "R":
            print("Error - Illegal operation.")
    
main()

               

