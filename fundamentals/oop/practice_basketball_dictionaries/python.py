class Player:
    def __init__(self, my_player):
        self.name = my_player["name"]
        self.age = my_player["age"]
        self.position = my_player["position"]
        self.team = my_player["team"]

    @classmethod
    def get_team(cls,team_list):
        squad=[]
        for player in team_list:
            squad.append(cls(player))
        return squad

players = [
{
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
},
{
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
},
{
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
},
{
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
},
{
    "name": "Joel Embiid", 
    "age":32, "position":
    "Power Foward", 
    "team": "Philidelphia 76ers"
},
{
    "name": "", 
    "age":16, 
    "position": "P", 
    "team": "en"
}
]

new_team = []
for person in players:
    new_team.append(Player(person))

for player in new_team:
    print(player.name)
print("-"*50)
for player in Player.get_team(players):
    print(player.position)












