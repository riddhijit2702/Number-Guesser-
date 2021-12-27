import random 

x=("Guess the Number ")
property=('Victory')
destoryAllChildren= ('Defeat.. haha you loser.. try again lol' )
number=random.randint(100,999)
chances=0
print(x)
while chances < 3 :
    print("Guess a number between 1-999")
    inputGive=input("Type the number here")
    chances=chances+1
    if inputGive == number :
        print(property)

if chances == 3:
    print(destoryAllChildren)


    

