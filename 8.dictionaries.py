#Dictionaries
#mapping iterable
#-declare
#-add/remove items
#-dict()
#-dir()
#-duck typing revisted

#there a lot of similaritioes between a dictionary and an object. a dictionary just has more power

book = {
    'title' :'Goodnight Moon', 
    'ratings': 700, 
    'stars': 4.5,
    'author': {'firstName': 'Mickey', 'lastName': 'Addao'},
    'images': ['goodnight.png', 'sleeptight.png']
    }
print(book)
print(len(book))
del book['stars'] #grabs the items and the key and deletes
print(book)
book['stars'] = 4.9
print(book)

for i in book:
    print(i, book[i])


#more ways to create dictionaries
pond = dict(
    depth=10, 
    area="210 sqaure feet",
    fish=["Mary", "Bob", "Billy"]
    )
print(pond)

alligator = dict([
    ('lifespan', 50), 
    ('length', 4),
    ('lengthUnits', 'm'),
    ('species',  ['American Alligator', 'Chinese Alligarot']),
    ('funfact', "As an alligator's teeth are worn down they are replaced")
])
print(alligator)

keys = ['name', 'home runs', 'strikeouts', 'rbi']
values = ['Babe Ruth', 7214, 1330, 2214]
player = dict(zip(keys, values)) #zip creates a dictionary from the two lists declares and maps key to value
print(player)
print(dir(player)) #metadata about the object