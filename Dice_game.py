import random
def roll():
    roll=random.randint(1,6)
    return roll
# print(roll())

while True:
    try:  
        players=int(input('Enter Number of players do you want (2-4): '))
        if 2<= players<=4:
            break
        else:
            print('Please Enter Players between 2 and 4')
    except:
        print('Please Enter a Valid Input')
players_score=[0 for _ in range(players)]
limit=4
for player in range(players):
    print('The Current is:',player+1)
    player_score=0
    for roll_num in range(1, limit + 1):
        input('Please Press Enter to Roll')
        dice_value = roll()
        player_score += dice_value
        
        print(f"Roll {roll_num}: 🎲 {dice_value} (Total: {player_score})")
        
    players_score[player]=player_score
    print(f"\n✅ Player {player + 1}'s Final Score: {player_score}")
    input("\nPress Enter to go to next player...")
    
max_score=max(players_score)
winners = [i + 1 for i, score in enumerate(players_score) if score == max_score]

print("\n" + "="*40)
print("🏆 GAME OVER - FINAL RESULTS 🏆")
print("="*40)

for i, score in enumerate(players_score):
    print(f"Player {i + 1}: {score} points")
    
print("="*40)

if len(winners) == 1:
    print(f"🎉 WINNER: Player {winners[0]} with {max_score} points! 🎉")
else:
    print(f"🎉 It's a TIE between Players {', '.join(map(str, winners))} with {max_score} points! 🎉")
