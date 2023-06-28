# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
#
# Examples:
# Input: 42145 Output: 54421
#
# Input: 145263 Output: 654321
#
# Input: 123456789 Output: 987654321


def descending_order(num):
    lst = []
    for i in str(num):
        lst.append(int(i))
    lst.sort()
    lst.reverse()
    num = ''
    for i in lst:
        num += str(i)
    num = eval(num)
    print(num)



descending_order(145263)