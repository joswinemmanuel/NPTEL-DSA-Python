""" Q) Here are some basic facts about tennis scoring: A tennis match is made up of sets. A set is made up of games.

To win a set, a player has to win 6 games with a difference of 2 games. At 6-6, there is often a special tie-breaker. In some cases, players go on playing till 
one of them wins the set with a difference of two games. Tennis matches can be either 3 sets or 5 sets. The player who wins a majority of sets wins the match 
(i.e., 2 out 3 sets or 3 out of 5 sets) The score of a match lists out the games in each set, with the overall winner's score reported first for each set. 
Thus, if the score is 6-3, 5-7, 7-6 it means that the first player won the first set by 6 games to 3, lost the second one 5 games to 7 and won the 
third one 7 games to 6 (and hence won the overall match as well by 2 sets to 1).
You will read input from the keyboard (standard input) containing the results of several tennis matches. Each match's score is recorded on a separate line with the 
following format:

Winner:Loser:Set-1-score,...,Set-k-score, where 2 ≤ k ≤ 5

For example, an input line of the form

Osaka:Barty:3-6,6-3,6-3
indicates that Osaka beat Barty 3-6, 6-3, 6-3 in a best of 3 set match.

The input is terminated by a blank line.

You have to write a Python program that reads information about all the matches and compile the following statistics for each player:

Number of best-of-5 set matches won
Number of best-of-3 set matches won
Number of sets won
Number of games won
Number of sets lost
Number of games lost
You should print out to the screen (standard output) a summary in decreasing order of ranking, where the ranking is according to the criteria 1-6 in that order
(compare item 1, if equal compare item 2, if equal compare item 3 etc, noting that for items 5 and 6 the comparison is reversed).

For instance, given the following data

Zverev:Medvedev:2-6,6-7,7-6,6-3,6-1
Barty:Osaka:6-4,6-4
Medvedev:Zverev:6-3,6-3
Osaka:Barty:1-6,7-5,6-2
Zverev:Medvedev:6-0,7-6,6-3
Osaka:Barty:2-6,6-2,6-0
Medvedev:Zverev:6-3,4-6,6-3,6-4
Barty:Osaka:6-1,3-6,7-5
Zverev:Medvedev:7-6,4-6,7-6,2-6,6-2
Osaka:Barty:6-4,1-6,6-3
Medvedev:Zverev:7-5,7-5
Osaka:Barty:3-6,6-3,6-3
your program should print out the following

Zverev 3 0 10 104 11 106
Medvedev 1 2 11 106 10 104
Osaka 0 4 9 76 8 74
Barty 0 2 8 74 9 76
You can assume that there are no spaces around the punctuation marks ":", "-" and ",". Each player's name will be spelled consistently and no two players 
have the same name."""

"""CODE"""

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
