vowels = frozenset("aeiou")

text = input("Please enter any text you'd like: ")

text_set = set(text)

for letter in vowels:
    if letter in text_set:
        text_set.remove(letter)

# opcion B:
# text_no_vowels = set(text).difference(vowels)


finalList = sorted(text_set)
print(finalList)