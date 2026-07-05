print('Welcome to Quizz Game!!')

choose=input('Do you Want to Play? ').lower()
if choose!='yes':
    quit()
else:
    print("Let's start")
score=0
answer=input('What does OTP means?').lower()
if answer=='one time password':
    print('Correct!!')
    score+=1
else:
    print('InCorrect')
answer=input('Who Created the Python?').lower()
if answer=='guido van rossum':
    print('Correct!!')
    score+=1
else:
    print('InCorrect')
answer=input('How Python Files are Saved? ').lower()
if answer=='.py':
    print('Correct!!')
    score+=1
else:
    print('InCorrect')
answer=input('Which function is used to display output on the screen? ').lower()
if answer=='print':
    print('Correct!!')
    score+=1
else:
    print('InCorrect')
answer=input('How many types of Variables are there? ').lower()
if answer=='two' or answer=='2':
    print('Correct!!')
    score+=1
else:
    print('InCorrect')
print(f'Your Score is {score}')
print('Thanks For Playing!!')
