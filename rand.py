#Write a Python script to add a key to a dictionary.
def add_key_to_dict(dictionary, key, value):
    dictionary [key] = value
    return dictionary
my_dict={'a': 1, 'b': 2, 'c': 3}
new_key = 'd'
new_value = 4

my_dict=add_key_to_dict(my_dict, new_key, new_value)
print("Updated dictionary:", my_dict)