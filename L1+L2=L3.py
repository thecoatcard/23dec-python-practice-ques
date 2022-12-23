# Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2?
# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
# odd_i = []
# even_i = []
# for i in range(0, len(l1)):
#     if i % 2!=0:
#         odd_i.append(l1[i])
# print(odd_i)
# for i in range(0,len(l2)):
#     if i % 2==0:
#         even_i.append(l2[i])
# print(even_i)
# l3 = odd_i + even_i
# print(l3)
# --------------------------------------------------------------------------------------------------------
# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
# list1 = [34, 54, 67, 89, 100, 43, 94]
# list1.pop(4)
# print(list1)
# list1.insert(2,11)
# print(list1)
# list1.insert(len(list1),11)
# print(list1)
# --------------------------------------------------------------------------------------------------------
# Slice list into 3 equal chunks and reverse each chunk
# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]


# def divide_chunks(l, n):
#     for i in range(0, len(l), n):
#         yield l[i:i + n]
# n=3
# x = list(divide_chunks(sample_list,n))
# print("Chunk_1",x[0])
# print(x[0][::-1])
# print("Chunk_2",x[1])
# print(x[1][::-1])
# print("Chunk_3",x[2])
# print(x[2][::-1])
# --------------------------------------------------------------------------------------------------------
# Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element.
# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# Create a dictionary to store the count of each element.
# sample_dict = {}
# for i in sample_list:
#     if i in sample_dict:
#         sample_dict[i] += 1
#     else:
#         sample_dict[i] = 1
# print(sample_dict)

# --------------------------------------------------------------------------------------------------------
# Find the intersection (common) of two sets and remove those elements from the first set.
# first_set = {23, 42, 65, 57, 78, 83, 29}
# second_set = {57, 83, 29, 67, 73, 43, 48}
# intersection = first_set.intersection(second_set)
# print(intersection)
# --------------------------------------------------------------------------------------------------------
# Checks if one set is a subset or superset of another set. If found, delete all elements from that set
# first_set = {27, 43, 34}
# second_set = {34, 93, 22, 27, 43, 53, 48}
# print("First set is subset of second set",first_set.issubset(second_set))
# print("Second set is subset of First set",second_set.issubset(first_set))
# print("First set is superset of second set",first_set.issuperset(second_set))
# print("Second set is superset of First set",second_set.issuperset(first_set))
# --------------------------------------------------------------------------------------------------------
# Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list.
# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
# for roll in roll_number:
#     if roll not  in sample_dict:
#         roll_number.remove(roll)
# print(roll_number)
# --------------------------------------------------------------------------------------------------------
# Get all values from the dictionary and add them to a list but don’t add duplicates.
# speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
# speed_list = list(speed.values())
# speed_list = list(set(speed_list))
# print(speed_list)
# ---------------------------------------------------------------------------------------------------------
# Remove duplicates from a list and create a tuple and find the minimum and maximum number.
# sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
# unique items in sample_list.
# unique_items = list(set(sample_list))
# print(unique_items)
# tuple items in sample_list.
# sample_tuple = tuple(unique_items)
# print(sample_tuple)
# find the minimum and maximum number in sample_tuple.
# min = min(sample_tuple)
# max = max(sample_tuple)
# print(min)
# print(max)
# ---------------------------------------------------------------------------------------------------------
# Convert two lists into a dictionary.
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dictionary = dict(zip(keys, values))
# print(dictionary)
# ------------------------------------------------------------------------------------------------------
#  Merge two Python dictionaries into one.
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict3 = dict1.copy()
# dict3.update(dict2)
# print(dict3)
# ------------------------------------------------------------------------------------------------------
# Print the value of key ‘history’ from the below dict.
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# print(sampleDict["class"])

# ------------------------------------------------------------------------------------------------------
#  Initialize dictionary with default values.
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# #initialize the keys with the same values.
# employees_with_defaults = dict(zip(employees,defaults.values()))
# print(employees_with_defaults)
# ------------------------------------------------------------------------------------------------------
# Create a dictionary by extracting the keys from a given dictionary.
# sample_dict = {
#     "name": "Kelly",
#     # "age": 25,
#     "salary": 8000,
#     # "city": "New york"
#     }

# keys = ["name", "salary"]
# keys_list = list(sample_dict.keys())

# values = ["Kelly", 8000]
# values_list = list(sample_dict.values())

# key_value_pairs = list(zip(keys_list, values_list))
# print(key_value_pairs)

#-----------------------------------------------------------------------------------------------------------
#  Delete a list of keys from a dictionary.
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# #  Delete a list of keys from a dictionary.
# del sample_dict["name"]
# del sample_dict["salary"]
# print(sample_dict)


#----------------------------------------------------------------------------------------------------------

# Check if a value exists in a dictionary.
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# print(sample_dict.get('b') ,"present in a dict")

# ----------------------------------------------------------------------------------------------------------
# Rename key of a dictionary.
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# sample_dict["location"]=sample_dict["city"]
# del sample_dict["city"]
# print(sample_dict)
# ---------------------------------------------------------------------------------------------------------
# Get the key of a minimum value from the following dictionary.
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# print(min(sample_dict, key=sample_dict.get))
# ---------------------------------------------------------------------------------------------------------
# Change value of a key in a nested dictionary.
# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500},
# }
# print(sample_dict)

