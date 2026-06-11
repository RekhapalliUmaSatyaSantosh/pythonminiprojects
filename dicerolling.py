import random

print("🎲 Dice Roller 🎲")
rolls = 0

while True:
    choice = input('\nRoll the dice? (y/n): ').lower()
    
    if choice == 'y':
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        rolls += 1
        
        # Visual dice representation
        dice = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']
        print(f'  {dice[d1-1]} {dice[d2-1]}  →  ({d1}, {d2})')
        
        # Special messages
        if d1 == d2:
            print(f'  🎉 DOUBLES! (Roll #{rolls}) 🎉')
        elif d1 + d2 == 7:
            print(f'  ✨ LUCKY 7! ✨')
        elif d1 + d2 == 2:
            print(f'  💀 SNAKE EYES! 💀')
            
    elif choice == 'n':
        print(f'\nYou rolled {rolls} time{"s" if rolls != 1 else ""}')
        print('Thanks for playing! 🎲')
        break
    else:
        print('❌ Please enter y or n')
