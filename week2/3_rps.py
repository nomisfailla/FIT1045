from random import *

# paper beats rock
# scissors beats paper
# rock beats scissors
def beats(a, b):
    if a == "paper" and b == "rock":
        return True
    elif a == "scissors" and b == "paper":
        return True
    elif a == "rock" and b == "scissors":
        return True
    else:
        return False

player = input("what is your choice: ")
computer = ["rock", "scissors", "paper"][randrange(0, 3)]

print("your opponent chose " + computer)

if player == computer:
    print("draw!")
else:
    if(beats(player, computer)):
        print("you win!")
    else:
        print("you lose")
        
