a = "Hello, World"
print(len(a))
txt = "My name is Nik"
print("Nik" in txt)

# string formatting
quantity = 3
item_no = 567
price = 49.95
my_order = "I want {} pieces of item {} for {} dollars."
print(my_order.format(quantity, item_no, price))

print(a.replace("H", "J"))

print("red" == "blue" or 3 >= 3)


def bool_to_word(boolean):
    if boolean:
        print("Yes")
    else:
        print("No")
    return boolean


print(bool_to_word(True))
print(bool_to_word(False))


