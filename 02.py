# Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2?
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
odd_i = []
even_i = []
for i in range(0, len(l1)):
    if i % 2!=0:
        odd_i.append(l1[i])
print(odd_i)
for i in range(0,len(l2)):
    if i % 2==0:
        even_i.append(l2[i])
print(even_i)
l3 = odd_i + even_i
print(l3)




