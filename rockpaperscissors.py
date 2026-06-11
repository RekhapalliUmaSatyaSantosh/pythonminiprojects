import random

emojis = {'r': '🪨', 'p': '📃', 's': '✂️'}
choices = ('r', 'p', 's')
player_score = 0
computer_score = 0

while True:
    user_choice = input('\nEnter (r)ock/(p)aper/(s)cissors: ').lower()

    if user_choice not in choices:
        print('Please enter r, p, or s')
        continue
        
    computer_choice = random.choice(choices)
    print(f'You chose: {emojis[user_choice]}')
    print(f'Computer chose: {emojis[computer_choice]}')
    
    if user_choice == computer_choice:
        print('Tie!')
    elif (user_choice == 'r' and computer_choice == 's') \
         or (user_choice == 's' and computer_choice == 'p') \
         or (user_choice == 'p' and computer_choice == 'r'):
        print('🎉 Player Wins! 🎉')
        player_score += 1
    else:
        print('💻 Computer Wins! 💻')
        computer_score += 1
    
    print(f'Score - You: {player_score} | Computer: {computer_score}')
    
    if input('Play again? (y/n): ').lower() in ['n', 'no']:
        print(f'\nFinal Score - You: {player_score} | Computer: {computer_score}')
        print('Thanks for playing!')
        break
