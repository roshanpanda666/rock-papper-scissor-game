import random
computer=random.randrange(1, 4)
points=0
copoints=0
i=0
while i<=5:
    i=i+1
    user=int(input("chose 1 for rock\nchose 2 for papper \nchose 3 for scissor"))

    if(computer==1):
        print("computer chosen rock")
    if(computer==2):
        print("computer chosen papper")
    if(computer==3):
        print("computer chosen scissor")

    if(user==computer):
        print("the game has been tie")

    elif(user==1):
        if(computer==3):
            print("rock smashes scissor you won the game")
            points+=1

            
        else:
            print("papper covers the rock computer won the game")
            copoints+=1

    elif(user==2):
        if(computer==1):
            print("papper covers the rock you won the game")
            points+=1
        else:
            print("scissor cutted papper computer won the game")
            copoints+=1

    elif(user==3):
        if(computer==2):
            print("scissor cutted papper you won")
            points+=1
        else:
            print("rock destroyed scissor you loss")
            copoints+=1

    else:
        print("enter the valid input")

print("you won the game",points,"times")
print("computer won the game",copoints,"times")
if(points>copoints):
    print("congrats you won the round in",points,"points")
elif(points==copoints):
    print("the game has been tie")
elif(copoints>points):
    print("computer won the round in",copoints,"points")
    print("you lose the game try again")
