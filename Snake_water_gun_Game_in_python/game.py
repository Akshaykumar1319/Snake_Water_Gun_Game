'''
1 : Snake
-1 : Water
0 : Gun
'''
import random

computer = random.choice([-1,0,1])

user = input("Enter Your choice : ")

myDict = {"s":1,"w":-1,"g":0}

reverseDict = {1:"Snake",-1:"Water",0:"Gun"}

choice = myDict[user]

print(f"Computer choice {reverseDict[computer]}\nYour choice {reverseDict[choice]} ")

if(computer == choice):
    print("Draw!")
else:
    if(computer == -1 and choice == 1):
        print("You win!")
    elif(computer == -1 and choice == 0):
        print("You loose!")
    elif(computer == 1 and choice == -1):
        print("You loose")
    elif(computer == 1 and choice == 0):
        print("You win!")
    elif(computer == 0 and choice == -1):
        print("You win")
    elif(computer == 0 and choice == 1):
        print("You loose!")
    else:
        print("Something is fishy here")