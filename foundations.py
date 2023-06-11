## FOUNDATIONAL CONCEPTS FOR PYTHON ##

# Variables #
my_int_var = 15
my_float_var = 12.5
my_str_var = 'red'
lst_of_things = ['shoe', 47, ['cat', 'dog', 'rabbit'], 3.14]
dict_of_things = {
    'clothing': 'shoe',
    'number': 47,
    'list of animals': ['cat', 'dog', 'rabbit'],
    'float': 3.14
}

## PRO TIP - avoid using full names of identified variable types like string, list, dictionary, and number ##

# If/Else Statements #
if my_int_var > 18:
    print('You can enter the movie!')
elif my_int_var >= 12:
    print('another comment')
elif my_int_var >= 15:
    print('Barely made it! Come on into the movie.')
else:
    print('You are not old enough to see this film. SORRY!')

# Lists #
my_food_lst = ['chocolate', 'cheese steak', 'pizza', 'fries']

# items in a list are indexed starting with number 0
print(my_food_lst[2])
# to add to the end of a list, use append() method
my_food_lst.append('burgers')
# to add to the beginning of a list use index 0, and change the index number to insert at any index value
my_food_lst.insert(0, 'cake')
# to remove the last item of a list, use pop() method which also accepts an index number to remove other elements in
# the list
my_fav_food = my_food_lst.pop(2)

print(my_food_lst, my_fav_food)

# Looping through Lists #
# for food in my_food_lst:
    # print(food)
    # if food == 'cake':
    #     print(f'{food} my favorite!')
    # elif food != 'burgers':
    #     print(f'Not craving {food} today')

# Dictionaries #
my_landmark_dict = {
    'Chicago': 'Willis Tower',
    'New York': 'Statue of Liberty',
    'Seattle': 'The Needle'
}

# To access values in dictionary, index the key name
print(my_landmark_dict['Chicago'])
# To access the keys or values in a dictionary, use the keys() or values() methods
print(my_landmark_dict.keys(), my_landmark_dict.values())
# To see all the key/value pairs in the dictionary, use the items() method
print(my_landmark_dict.items())

# Looping through Dictionaries #
# default loop is keys
for cities in my_landmark_dict:
    print(cities)
# must use method to access the values specifically
for landmark in my_landmark_dict.values():
    print(landmark)
for key, value in enumerate(my_landmark_dict.items()):
    print(key, value)

# to add to dictionaries use update() method
my_landmark_dict.update({'St. Louis': 'Arch'})
print(my_landmark_dict)
