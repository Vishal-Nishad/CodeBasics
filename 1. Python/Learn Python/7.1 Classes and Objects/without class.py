import datetime

virat={
    "first":'virat',
'last':'kholi',
'birthyear':1988,
    "scores":[]
}
virat["scores"].append(100)
virat["scores"].append(67)
virat["scores"].append(0)

def get_average_score(player):
    average=sum(player['scores'])/len(player['scores'])
    print(sum(player['scores']))
    print(len(player['scores']))
    return average
def get_age(player):
    current_year=datetime.datetime.now().year
    print(current_year)
    return current_year - player['birthyear']
print(get_average_score(virat))
print((get_age(virat)))