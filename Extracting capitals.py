quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
capitals = ""
for char in quote:
    if char.isupper():
        capitals = capitals + char

print(capitals)


for i in range(21):
    if i == 0 or i % 3 == 0 or i % 5 == 0:
        continue
    print(i)