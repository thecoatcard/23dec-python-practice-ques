# ---------------------------------------------------------------------------------------------------------
# Remove duplicates from a list and create a tuple and find the minimum and maximum number.
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
# unique items in sample_list.
unique_items = list(set(sample_list))
print(unique_items)
# tuple items in sample_list.
sample_tuple = tuple(unique_items)
print(sample_tuple)
# find the minimum and maximum number in sample_tuple.
min = min(sample_tuple)
max = max(sample_tuple)
print(min)
print(max)