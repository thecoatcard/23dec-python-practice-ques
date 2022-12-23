
# ------------------------------------------------------------------------------------------------------
# Create a dictionary by extracting the keys from a given dictionary.
sample_dict = {
    "name": "Kelly",
    # "age": 25,
    "salary": 8000,
    # "city": "New york"
    }

keys = ["name", "salary"]
keys_list = list(sample_dict.keys())

values = ["Kelly", 8000]
values_list = list(sample_dict.values())

key_value_pairs = list(zip(keys_list, values_list))
print(key_value_pairs)
