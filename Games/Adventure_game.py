import time

print('='*40)
print('WELCOME TO THE FOREST ADVENTURE')
print('='*40)
input('Press Enter to Start.....')
print('\nYou wake up in a dark forest....')

while True:
    print('A. Go left toward the river')
    print('B. Go right toward the cave')
    choose = input('Enter your Choice: ').lower()

    if choose == 'a':
        print('\n--- RIVER SCENE ---')
        print('A. Swim across')
        print('B. Follow the river')
        choose = input('Enter your Choice: ').lower()
        
        if choose == 'a':
            print('\n🏊 You swim across the river...')
            time.sleep(3)
            print('You find a hidden treasure chest!')
            time.sleep(3)
            print('💰 Congratulations! You found treasure! 💰')
            time.sleep(3)
            print('🎉 YOU WIN! 🎉')
        
        elif choose == 'b':
            print('\n🚶 You follow the river...')
            time.sleep(3)
            print('You find a friendly bear eating berries.')
            time.sleep(3)
            print('The bear shares its berries with you.')
            time.sleep(3)
            print('You become friends and it shows you the way out!')
            time.sleep(3)
            print('🎉 YOU ESCAPE SAFELY! 🎉')
        
        else:
            print('❌ Invalid choice!')

    elif choose == 'b':
        print('\n--- CAVE SCENE ---')
        print('A. Enter the cave')
        print('B. Run away')
        choose = input('Enter your Choice: ').lower()
        
        if choose == 'a':
            print('\n🐉 You enter the dark cave...')
            time.sleep(3)
            print('A dragon wakes up and sees you!')
            time.sleep(3)
            print('💀 GAME OVER! The dragon wins! 💀')
        
        elif choose == 'b':
            print('\n🏃 You run away quickly...')
            time.sleep(3)
            print('You find a hidden path and escape the forest!')
            time.sleep(3)
            print('🎉 YOU SURVIVE! 🎉')
        
        else:
            print('❌ Invalid choice!')

    else:
        print('❌ Invalid choice!')

    again = input("\nUse another tool? (y/n): ").lower()
    if again != 'y':
        print('\nThanks for playing!')
        break
