import random

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100\n")

d = random.randint(1, 100)
guesses = 0

while True:
    try:
        n = int(input('Your guess: '))
        guesses += 1
        
        if n == d:
            print(f'\n✅ Correct! The number was {d}')
            print(f"📊 You got it in {guesses} guess{'es' if guesses != 1 else ''}")
            break
        elif n < d:
            print('📉 Too Low - Try higher!')
        else:
            print('📈 Too High - Try lower!')
            
        # Give hint after 5 wrong guesses
        if guesses == 5 and n != d:
            print(f"💡 Hint: The number is {'odd' if d % 2 else 'even'}")
            
    except ValueError:
        print('❌ Please enter a valid integer!')

print('\nThanks for playing! 🎮')
