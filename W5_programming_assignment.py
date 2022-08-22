data=input()
result={}
while data:
    winner, loser, sets = data.split(':')
    winner_sets, loser_sets = 0, 0
    winner_games, loser_games = 0, 0 
    winner_BO5, winner_BO3 = 0, 0
    
    for i in sets.split(','):
        score = list(map(int, i.split('-')))
        
        if score[0] > score[1]:
            winner_sets += 1
        else:
            loser_sets += 1

        winner_games += score[0]
        loser_games += score[1]

    if winner_sets >= 3:
        winner_BO5 += 1
    else:
        winner_BO3 += 1

    if winner not in result:
      result[winner] = [0, 0, 0, 0, 0, 0]
    if loser not in result:
      result[loser] = [0, 0, 0, 0, 0, 0]
    
    result[winner][0] += winner_BO5
    result[winner][1] += winner_BO3
    result[winner][2] += winner_sets
    result[winner][3] += winner_games
    result[winner][4] += loser_sets
    result[winner][5] += loser_games

    result[loser][2] += loser_sets
    result[loser][3] += loser_games
    result[loser][4] += winner_sets
    result[loser][5] += winner_games

    data=input()   

result = sorted(result.items(), key=lambda t:t[1], reverse=True)

for player in result:
    print(f"{player[0]} {player[1][0]} {player[1][1]} {player[1][2]} {player[1][3]} {player[1][4]} {player[1][5]}")
