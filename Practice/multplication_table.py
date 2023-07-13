number = int(input("Select a number: "))

for count in range(1, 11):
    product = number * count
    print(number, "x", count, "=", product)