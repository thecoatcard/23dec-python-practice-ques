# --------------------------------------------------------------------------------------------------------
# Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element.
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

sample_dict = {}
for i in sample_list:
    if i in sample_dict:
        sample_dict[i] += 1
    else:
        sample_dict[i] = 1
print(sample_dict)