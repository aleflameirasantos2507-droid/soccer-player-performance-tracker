players = []
goals = []
player = {}

while True:
    total_goals = 0

    player['name'] = input('Name: ').capitalize()

    matches = int(input(f"How many matches did {player['name']} play? "))

    for match in range(1, matches + 1):
        goals_scored = int(input(f'Goals scored in match {match}: '))
        goals.append(goals_scored)
        total_goals += goals_scored

    player['goals'] = goals[:]
    player['total'] = total_goals

    players.append(player.copy())
    goals.clear()

    option = input('Would you like to continue? ').strip().upper()[0]

    if option == 'N':
        break

print(f'{"Code":<6}{"Name":<15}{"Goals":<20}{"Total":>7}')
print('=' * 50)

for index, player in enumerate(players):
    print(f'{index:<6}{player["name"]:<15}{str(player["goals"]):<20}{player["total"]:>7}')

print('=' * 50)

while True:
    player_code = int(input('Show data for which player? [999 to stop] '))

    if player_code == 999:
        print('ENDING PROGRAM...')
        break

    if 0 <= player_code < len(players):
        print('=' * 30)
        print(f'Performance report for {players[player_code]["name"]}:')

        for match, goals in enumerate(players[player_code]['goals'], start=1):
            print(f'Match {match}: {goals} goal(s)')
