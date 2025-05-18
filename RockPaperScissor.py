import random

choices=["rock", "paper", "scissor"]

rounds= input("enter how many rounds u want to play ><  :")

if not rounds.isdigit():
    print("enter a valid number please:")
    exit()

rounds= int(rounds)
player_score=0
computer_score=0    

for i in range(rounds):
    print(f"\n Rounds {i+1} of {rounds}")

    player_choice= input("enter rock or scissor or paper:").lower()
    if player_choice not in choices:
        print("enter a valid choice!!!")
        computer_score=computer_score+1
        continue


    computer_choice= random.choice(choices)    
    print(f"computer chose:{computer_choice}")

    if player_choice==computer_choice:
        print("its a tie")

    elif (
        (player_choice=="rock" and computer_choice=="scissor") or
        (player_choice=="scissor" and computer_choice=="paper") or
        (player_choice=="paper" and computer_choice=="rock")

    ):
        print(" -----------------you win this round!! :) -----------------")
        player_score+=1
    else:
        print("----------------- you lost this round :( ---------------------")
        computer_score+=1

print("\n------final scores:---------") 
print(f"you:{player_score}")
print(f"opponent:{computer_score}")

if player_score>computer_score:
    print("YAY YOU WON THE GAME!")
elif player_score<computer_score:
    print("GURLL WHAT'S THIS? YOU LOST :( GOTTA WIN!! SO PLAY AGAIN :p")
else:
    print ("YOU TIED HEHEHE")    