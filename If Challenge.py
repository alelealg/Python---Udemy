name = input("Please write your name: ")
age = int(input("Please enter your age: "))

if age > 17 and age < 31:
    print("{}, since you are {} years old, you can go on holiday.".format(name, age))
else:
    print("{}, since you are {} years old, you are not on the right age group.".format(name, age))