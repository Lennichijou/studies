import csv
FILENAME = "players.csv"
RESULTS = "results.csv"
players = []
results = []

def sortSecond(array):
    return array[1]

with open(FILENAME, "r", encoding="utf8", newline="") as file:
    reader = csv.reader(file)
    data = list(reader)
file.close()

del data[0]
for player in data:
    players.append([player[0], int(player[1])+int(player[2])])    
players.sort(key=sortSecond, reverse=True)
for player in players:
    results.append([player[0], 1])

n = 1
for i in range(1, len(players)):
    if players[i-1][1] > players[i][1]:
        results[i][1] = n+1 
    elif players[i-1][1] == players[i][1]:
        results[i-1][1] = n
        results[i][1] = n
    n+=1
#print(*results)

with open(RESULTS, "w", encoding="utf8", newline="") as resfile:
    columns = ["Спортсмен", "Место"]
    writer = csv.writer(resfile)
    writer.writerow(columns)
    for i in range(len(results)):
        writer.writerow([results[i][0], results[i][1]])
resfile.close()

with open(RESULTS, "r", encoding="utf8", newline="") as file:
    for row in csv.reader(file):
        print(row)
