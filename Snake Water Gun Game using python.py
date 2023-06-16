#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gorisha bhawsar
#
# Created:     16/06/2023
# Copyright:   (c) Gorisha bhawsar 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
comp = random.randint(0,2)

def check(comp, user):

    if(comp == user):
        return 0

    if(comp == 0 and user == 1):
        return -1

    if(comp == 2 and user == 0):
        return -1

    if(comp == 1 and user == 2):
        return -1

    return 1

user = int(input('Enter 0 for Snake , 1 for Water , 2 for Gun'))

Score = check(comp, user)

print("You", user)
print("Computer", comp)

if(Score == 0):
    print("Its a Draw!!")

elif(Score == -1):
    print("Better Luck Next Time :)")

else:
    print("Yayyy! You Won!!!")