# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
#
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)
#
# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)
#
# Note: The function accepts an integer and returns an integer.
#
# Happy Coding!

def square_digits(num):
    # new list for string to get unpacked into a list
    numbers_string = []
    # list as integers
    numbers_num = []
    # add the characters into the list
    for i in str(num):
        numbers_string.append(i)
    # convert to int, and add to int list
    for i in numbers_string:
        i = int(i)
        i *= i
        numbers_num.append(i)
    # answer variable, currently blank
    answer = ''
    # add each character to the answer variable, stored as a string
    for i in numbers_num:
        answer = answer + str(i)
        i += 1
    # eval will remove the quotations from the beginning and end of the string
    answer1 = eval(answer)
    return answer1


# pass in the function
square_digits(9119)