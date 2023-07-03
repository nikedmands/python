#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
print(Belgium)
print('')

# 3a
# hyphens the same length as the Belgium string
print('Question 3a')
print('-' * len(Belgium))
print('')

# 3b
# commas, replaced by colons ':'
print('Question 3b')
print(Belgium.replace(",", ":"))
print('')

# 3c
# population of Belgium (2nd field), plus the population of capital city (4th field) - should be 11183818
print('Question 3c')
# create split (creates new list) of each item, separated by a comma (',')
a = Belgium.split(",")
print(a)
# b = index 1 of a (new list) converted to an integer
b = int(a[1])
# b = index 3 of a (new list) converted to an integer
c = int(a[3])
print(b + c)

