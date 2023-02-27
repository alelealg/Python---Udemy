menu = "These are the options: " \
       "\n 1.\tLearn Python " \
       "\n 2.\tLearn Java " \
       "\n 3.\tGo swimming"\
       "\n 4. Have dinner " \
       "\n 5.\tGo to bed " \
       "\n 0.\tExit"
print(menu)

while True:
    option_chosen = input("What do you want to do? ")
    if option_chosen == "0":
        print("You chose option {}. You quit, you loser".format(option_chosen))
        break
    elif option_chosen in "12345":
        print("You chose option #{}.".format(option_chosen))
    else:
        print("That is not a valid choice. \n" +
              menu)



