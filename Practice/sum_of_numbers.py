# empty numbers list
numbers = []
# enter low number
low_num = input('Please enter the low number: ')
# convert to an int
low_num = int(low_num)
# enter high number
high_num = input('Please enter the high number: ')
# convert to an int
high_num = int(high_num)

# run while loop, i.e. don't finish making the list until the high number is in there
while high_num not in numbers:
    # add low number to the list
    numbers.append(low_num)
    # add low number +1 to the list
    low_num += 1

# add all numbers together in the list
print("Sum of the list =", sum(numbers))
print('')
# print the list
print("List looks as follows:")
print(numbers)
