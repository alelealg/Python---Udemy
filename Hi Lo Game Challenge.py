low = int(input("Please enter the lowest number in interval: "))
high = int(input("Please enter the lowest number in interval: "))
print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start.")

guesses = 1
while low != high:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. This is guess # {}. "
                     "Should I guess higher or lower? "
                     "Please enter 'h', 'l', or 'c' if I guessed correctly "
                     .format(guess, guesses)).casefold()
    if high_low == "h":
        low = guess + 1
        guesses += 1
    elif high_low == "l":
        high = guess - 1
        guesses += 1
    elif high_low == "c":
        print("I guessed correctly! It took me {} tries".format(guesses))
        break
    else:
        print("Please enter correct info.")
else:
    print("You thought of the number {}.".format(low))
    print("I guessed in {} tries".format(guesses))


