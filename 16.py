#-----------------------------------------------------------------------------------------------------------
#  Delete a list of keys from a dictionary.
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
#  Delete a list of keys from a dictionary.
del sample_dict["name"]
del sample_dict["salary"]
print(sample_dict)