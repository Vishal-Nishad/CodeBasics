import datetime
class player:       ## Parent class
    def __init__(self,fname,lname,birthyear):
        self.firstname = fname
        self.lastname = lname
        self.birthyear = birthyear

    def get_age(self):
        current_age = datetime.datetime.now().year
        return current_age - self.birthyear

class tennis_player(player):   ## Child Class
    def __init__(self,fname,lname,birthyear):
        super().__init__(fname,lname,birthyear)
        self.scores = []
"""
When Overriding __init__:
When you define your own __init__ in the child class (as is common 
when you want to extend the parent's behavior), the parent's __init__ 
is not automatically called.
Without explicitly calling super().__init__(...), the initialization 
code in the parent’s __init__ would be skipped, meaning the parent’s 
attributes (like firstname, lastname, and birthyear in your example) 
might never be set up on the child object.

Example Without Calling super():

class tennis_player(player):  # Inherits from player
    def __init__(self, fname, lname, birthyear):
        # Forgot to call super().__init__(...)
        self.scores = []  # Only sets up tennis-specific attribute

"""
    def add_scores(self,score):
        self.scores.append(score)
    def get_average(self):
        return sum(self.scores)/len(self.scores)
rogic = tennis_player('rogic','fed',1990)
rogic.add_scores(45)
rogic.add_scores(55)
print(rogic.get_average())
print(rogic.lastname)