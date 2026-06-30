import random
import time

secert_num=random.randint(1000, 10000)
attempts=0

print('='*40)
print('     Welcome to Master Mind game!!')
print('='*40)
print("Try to guess the 4-digit number.\n")

start_time=time.time()
while True:
    
    try:
        guess=int(input('Enter number to guess= '))
        if guess<1000 or guess>9999:
            print('Please enter 4 digit number')
            continue
    except ValueError:
        print('Enter valid number')
        continue
        
    attempts+=1
    if guess==secert_num:
        end_time=time.time()
        print('='*40)
        print('     🎉 CONGRATULATIONS! 🎉\n You have guessed number correctly!')
        print('='*40)
        print(f"It took you only {attempts} tries.")
        print(f'⏱️ Time taken: {end_time - start_time:.2f} seconds')
        print('='*40)
        break
    guess_num=str(guess)
    secert=str(secert_num)
    
    correct_count=0
    place=['X']*4
    for i in range(4):
        if guess_num[i]==secert[i]:
            correct_count+=1
            place[i]=guess_num[i]
    print(f"\nNot quite the number. You did get {correct_count} digit(s) correct.")
    
    misplaced_count=0
    secert_copy=list(secert)
    for i in range(4):
        if guess_num[i]==secert[i]:
            secert_copy[i]=None
            
    for i in range(4):
        if guess_num[i] != secert[i] and guess_num[i] in secert_copy:
            misplaced_count += 1
            secert_copy[secert_copy.index(guess_num[i])] = None
    
    print(f"\n📊 {correct_count} digit(s) in the correct position.")
    if misplaced_count > 0:
        print(f"🔄 {misplaced_count} digit(s) correct but in the wrong position.")
    
    if correct_count>0:
        print('Correctly placed.')
        print(" ".join(place))
    print()
