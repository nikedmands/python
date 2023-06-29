numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares_list = list(map(lambda num: num ** 2, numbers))
print(squares_list)
even_list = list(filter(lambda num: num % 2 == 0, numbers))
print(even_list)