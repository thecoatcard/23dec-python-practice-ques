# --------------------------------------------------------------------------------------------------------
# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
list1 = [34, 54, 67, 89, 100, 43, 94]
list1.pop(4)
print(list1)
list1.insert(2,11)
print(list1)
list1.insert(len(list1),11)
print(list1)