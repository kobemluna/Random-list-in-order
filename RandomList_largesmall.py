# Kobe Luna
# StudentID= 21590963
# Homework 1, problem 3

import random 

Start=1000
Stop=2000
Limit=20

RandomList=[random.randint(1000,2000) for iter in range (Limit)]

print (RandomList)

largest1=RandomList[0]
smallest1=RandomList[0]
largest2=None
smallest2=None

for item in RandomList[1:]:
    if item > largest1:
        largest2=largest1
        largest1=item
    elif largest2==None or largest2<item:
        largest2=item
    if item < smallest1:
        smallest2=smallest1
        smallest1=item
    elif smallest2==None or smallest2>item:
        smallest2=item

print("second largest number is : ", largest2)
print("second smallest number is : ", smallest2)
