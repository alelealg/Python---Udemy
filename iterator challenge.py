list_h18 = ["ale", "ricardo", "sinco", "uno"]

my_iterator_h18 = iter(list_h18)

for person in range(0, len(list_h18)):
    print(next(my_iterator_h18))


o = range(0, 100, 4)
for i in o:
    print(i)
print("*"*50)
p = o[::5]
for i in p:
    print(i)