import random

lowest = int(input("Choose lowest: "))
highest = int(input("Choose highest: "))
answer = random.randint(lowest, highest)

print(answer) #TODO: erase after testing

guess = int(input("Please choose number between {} and {}: ".format(lowest, highest)))

while guess != answer:
    if guess < answer:
        guess = int(input("Please guess higher: "))
    if guess > answer:
        guess = int(input("Please guess lower: "))
    if guess == 0:
        print("You quit, loser!")
        break

if guess == answer:
    print("Congratulations, you guessed correctly")