'''
File: bball.py
Author: Lane Molsbee
Course: CSC 120, Spring 2024
Purpose: This program contains three classes,
Team, Conference, and ConferenceSet.
The Team class represents a sports team and includes
the various attributes associated with that team.
Conference is a list of Team objects that 
represent a particular sports conference.
ConferenceSet represents a list of Conferences.
The program is designed to find the conferences
with the best average win ratios for
all the teams that were part of that conference. 
'''
class Team:
    '''
    This class represents a sports teams. 
    The primary methods are __init__, the constructor,
    as well as name, conf, and win_ratio,
    which are important to the overall functioning
    of these programs. 
    It is to be constructed using a list
    representing various facts associated with
    the sports team. 
    The Team class is an important foundation
    for the Conference class, which is important
    for the ConferenceSet class. This class
    forms the basis for overall program functioning. 
    '''
    def __init__(self, line):
        '''
        This is the constructor for the Teams class.
        Parameters: line is a list containing
        facts associated with the sports team.
        Returns: nothing
        '''
        # Assume line is a list
        # The list elements are assumed to be standardized.
        team_name = line[0]
        conf_name = line[1]
        wins = line[2]
        losses = line[3]       
        self._team = team_name
        self._conf = conf_name
        self._wins = wins
        self._losses = losses

    def name(self):
        '''
        This function is a getter method. 
        Parameters: None
        Returns: the team name instance variable _team
        '''
        return self._team
    
    def conf(self):
        '''
        This function is a getter method. 
        Parameters: None
        Returns: the conference name instance variable
        '''
        return self._conf
    
    def win_ratio(self):
        '''
        Returns the float value win ratio for the team.
        Parameters: None
        Returns: the win ratio for the team. 
        '''
        # The formula is Wins / (Wins + Losses)
        return float(self._wins) / (float(self._wins) + float(self._losses))
    
    def __str__(self):
        '''
        This is the str method for the class.
        Parameters: none
        Returns: the string representation of a Team object
        '''
        return "{} : {}".format(self._team, self.win_ratio())

class Conference:
    '''
    This class represents a Conference of teams. 
    The primary methods are __init__, __contains__,
    and win_ratio_avg, the last of which is important
    to the functioning of the program's purpose. 
    It is to be constructed using only the 
    name of the conference in question. 
    This class is never directly used by
    the user in the main() method
    but is instead relied on by the 
    ConferenceSet class which is what fulfills
    the overall purpose of the program. 
    '''
    def __init__(self, conf):
        '''
        This is the class constructor. 
        Parameters: conf is a string representing
        the name of the conference
        Returns: Nothing
        '''
        self._conf = conf
        self._teams = []
    
    def __contains__(self, team):
        '''
        This is the special method for 
        determining if a team is in
        the conference. 
        Parameters: team is a team object
        Returns: a boolean determining
        whether the Team object is in
        the Conference team list. 
        '''
        for team_string in self._teams:
            if team_string == team:
                return True
        return False
    
    def name(self):
        '''
        This is a getter method.
        Parameters: None
        Returns: the value of the conference name
        '''
        return self._conf
    
    def add(self, team):
        '''
        This function adds a team to the list.
        Parameters: team is a Team object
        Returns: nothing
        '''
        self._teams.append(team)
    
    def win_ratio_avg(self):
        '''
        This function calculates the win ratio
        average for all the teams in the conference.
        Parameters: None
        Returns: a float value representing
        the win ratio, calculated by summing
        all the win ratios of the teams in
        the conference and dividing by the number
        of teams in the conference. 
        '''
        num_teams = len(self._teams)
        win_ratio_sum = 0
        for x in self._teams:
            win_ratio_sum += x.win_ratio()
        return float(win_ratio_sum) / float(num_teams)
    
    def __str__(self):
        '''
        This is the str method for the class. 
        Parameters: none
        Returns: a string representation of the object
        in the form "Conference Name :
        '''
        return "{} : {}".format(self._conf, self.win_ratio_avg())

    
    
class ConferenceSet:
    '''
    This class represents a set of Conferences.
    Its primary methods are __init__ and best,
    the latter of which is the main function of
    this program on the whole because it completes
    the main program function. 
    It is to be constructed using no parameters. 
    This class is the main class used in this program
    as it is what compares all the Conference
    objects and gets their best win ratios. 
    '''
    def __init__(self):
        '''
        This is the class constructor.
        Parameters: None
        Returns: Nothing
        '''
        self._confs = []
    
    def add(self, team):
        '''
        This function adds a Team to the
        appropriate Conference in the ConferenceSet,
        adding a new Conference object to the
        list if necessary. 
        Parameters: team is a Team object
        Returns: nothing
        '''
        # Create a list of Conference names to compare
        conf_names = []
        for conf in self._confs:
            conf_names.append(conf.name())
        if team.conf() not in conf_names:
            new_conf = Conference(team.conf())
            new_conf.add(team)
            self._confs.append(new_conf)
        else:
            for conf in self._confs:
                if team.conf() == conf.name():
                    conf.add(team)
    
    def best(self):
        '''
        This function determines the greatest
        average win ratio out of all the Conference
        objects and returns the list of all the 
        Conferences with that ratio as well as
        the ratio value itself. 
        Parameters: None
        Returns: a tuple wherein the first element
        is a list containing the Conference objects
        with the greatest average win ratio and the 
        second element is the value of that average. 
        '''
        highest_win_ratio = 0
        best_confs = []
        for conf in self._confs:
            if conf.win_ratio_avg() > highest_win_ratio:
                # Empty the list and start a new one
                best_confs = []
                best_confs.append(conf.name())
                highest_win_ratio = conf.win_ratio_avg()
            elif conf.win_ratio_avg() == highest_win_ratio:
                best_confs.append(conf.name())
        best_confs = sorted(best_confs)
        return (best_confs, highest_win_ratio)


def main():
    '''
    This is the main method that tests all the 
    above classes. 
    Parameters: None
    Returns: Nothing
    '''
    confs = ConferenceSet()
    file_name = input()
    file = open(file_name, "r")
    for line in file:
        # Ignore comment lines
        if line[0] != "#":
            # Remove all unnecessary characters
            elements = line.lstrip("1234567890")
            elements = elements.strip()
            # Break up lines into meaningful elements
            i = elements.rindex("(")
            j = elements.rindex(")")
            facts = []
            team_name = elements[:i]
            facts.append(team_name)
            conf_name = elements[i + 1 : j]
            facts.append(conf_name)
            scores = elements[j + 1:].split()
            wins = scores[0]
            facts.append(wins)
            losses = scores[1]
            facts.append(losses)

            new_team = Team(facts)
            confs.add(new_team)
    # Determine the best conferences and print
    best_confs = confs.best()
    for i in range(len(best_confs[0])):
        print(best_confs[0][i],":", best_confs[1])

main()

