import random
import time

operators=['+', '-', '*']
min=3
max=20
questions=int(input('Enter How many questions do you want= '))
def generate():
    left=random.randint(min,max)
    right=random.randint(min,max)
    oper=random.choice(operators)
    exper=str(left)+ " "+ oper + " " + str(right)
    answer=eval(exper)
    return exper, answer

wrong=0
start_time=time.time()
for i in range(questions):
    exper, answer=generate()
    
    while True:
        guess=input('Problem #'+ str(i+1)+ ':' + exper + '= ')
        if guess==str(answer):
            break
        wrong+=1
end_time=time.time()
total_time=round(end_time-start_time,2)
print('The Total time taken to complete questions=',total_time,'seconds')
