# cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]
#
# with open("cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)

cities = []

# with open("cities.txt", 'r') as city_file:
#     for city in city_file:
#         cities.append(city.strip('\n'))
#
# print(cities)
# for city in cities:
#     print(city)

# imelda = "More Mayhem", "Imelda May", "2011", (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town"))
#
# with open("imelda3.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)

# with open("imelda3.txt", 'r') as imelda_file:
#     contents = imelda_file.readline()
#
# imelda = eval(contents)
#
# print(imelda)
# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)


# m = re.search(r'ab[cd]?)', """acdeabdabcde""")
# m.groups()

# sys.path

# type(datetime.date(2012, 01, 01) - datetime.date(2011, 01,01))

import itertools

x = [i for i in filter(lambda x: x % 5, itertools.islice(itertools.count(5), 10))]
print(x)