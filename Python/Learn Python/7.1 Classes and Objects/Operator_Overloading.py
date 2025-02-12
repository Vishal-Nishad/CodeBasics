import datetime
class CricketPlayer :    ## Creating class
    team_size=11         ## Class attributes
## init method to initialize object properties when an object is created
    def __init__(self,name,last,birth,team):
        self.firstname = name
        self.lastname = last
        self.birthyear = birth
        self.scores=[]
        self.team=team

## ## Class methods

    def add_score(self,score):
        self.scores.append(score)
    def get_average(self):
        return sum(self.scores)/len(self.scores)
    def get_age(self):
        current_year=datetime.datetime.now().year
        return current_year - self.birthyear

    ## Operator Overloading
    def __lt__(self, other):
        self_average=self.get_average()
        other_average=other.get_average()
        return self_average<other_average


virat=CricketPlayer('virat','kholi',1988,'India')    ## Creating instance/ Object from class
virat.add_score(139)
virat.add_score(98)
virat.add_score(67)
print(virat.lastname)
print(virat.firstname)
print(virat.birthyear)
print(virat.team)
print(virat.scores)
print(virat.get_average())
print(virat.get_age())

david = CricketPlayer('david','warner',1990,'Australia')
david.add_score(50)
david.add_score(30)
david.add_score(45)

print(david<virat)