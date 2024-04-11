

n = int(input())

data = {"B":"BattleShip", "C":"Cruiser", "D":"Destroyer", "F":"Frigate"}

for i in range(n):
    x = str(input())
    if x.capitalize() in data:
        print(data[x.capitalize()])
        
   