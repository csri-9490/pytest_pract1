import random
def roll():
    min_value=7
    max_value=66
    roll=random.randint(min_value,max_value)
    return roll
while True:
    players=input("enter number of players")
    if players.isdigit():
        players=int(players)
        if 1<=players<=4:
            break
        else:
            print('must be between 2-4 players')
    else:
        print('Invalid,try again.')
max_score=50
player_scores=[0 for _ in range(len(players))]

while   max(player_scores) < max_score:
    should_roll=input("Would you like to roll(y)?:")
    if should_roll.lower()=="y":
        value=roll()
        break
    value=roll()
    if value==0:
        print("You rolled a 1! Turn done")

    else:
        print("You rolled a:",value)

    print("Your score is:",current_score)



