import random

# Rock = 1, paper = 2, scissors = 3
print("If you want to quit, input 'Quit'")
player = input("Please choose rock, paper or scissors: ")

while True:
    computer = random.randint(1, 3)
    player = player.casefold()
    if player == "rock":
        player = 1
    elif player == "paper":
        player = 2
    elif player == "scissors":
        player = 3
    elif player == "quit":
        player = 4
    else:
        player = 5
    if player == 5:
        player = input("Please enter valid input: ")
    if player == computer:
        player = input("Draw, go again: ")
    if player == 1 and computer == 2:
        player = input("Paper beats rock, you lose. Try again: ")
    if player == 1 and computer == 3:
        player = input("Rock beats scissors, you win! Play again: ")
    if player == 2 and computer == 3:
        player = input("Scissors beat paper, you lose. Try again: ")
    if player == 2 and computer == 1:
        player = input("Paper beats rock, you win! Play again: ")
    if player == 3 and computer == 1:
        player = input("Rock beats scissors, you lose. Try again: ")
    if player == 3 and computer == 2:
        player = input("Scissors beat paper, you win! Play again: ")
    if player == 4:
        print("You quit, you loser!")
        break
