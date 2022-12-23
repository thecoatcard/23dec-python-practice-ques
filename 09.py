# --------------------------------------------------------------------------------------------------------
# Get all values from the dictionary and add them to a list but don’t add duplicates.
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
speed_list = list(speed.values())
speed_list = list(set(speed_list))
print(speed_list)