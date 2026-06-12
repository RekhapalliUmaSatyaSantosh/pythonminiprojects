import random
word_bank = ["monkey", "python", "hangman", "computer", "programming"]
secret_word = random.choice(word_bank).lower()
guessed_letter = []
attempts = 6
wrong = 0
display = ['_'] * len(secret_word)
while True:
    print("Word: " + " ".join(display))
    print("Guessed: " + " ".join(guessed_letter))
    print(f"Attempts left: {attempts - wrong}")
    print()
    guess = input('Enter a letter to guess: ').lower()
    if len(guess) != 1:
        print('Please enter exactly ONE letter\n')
        continue
    if not guess.isalpha():
        print("Enter a LETTER (a-z)\n")
        continue
    if guess in guessed_letter:
        print(f"You already guessed '{guess}'\n")
        continue
    guessed_letter.append(guess)
    if guess in secret_word:
        print(f"✅ Yes! '{guess}' is in the word!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess.upper()
    else:
        print(f"❌ No! '{guess}' is NOT in the word!\n")
        wrong += 1
    if "_" not in display:
        print("🎉 YOU WIN! 🎉")
        print(f"The word was {secret_word.upper()}")
        break
    if wrong == attempts:
        print("💀 GAME OVER! 💀")
        print(f"The word was {secret_word.upper()}")
        break
