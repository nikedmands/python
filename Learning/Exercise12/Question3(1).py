import random
# random.sample generates unique samples (multiple items) from a sequence without repetition
# range, between 1 - 50, 6 times
lotto_numbers = random.sample(range(1, 50), 6)
print(lotto_numbers)
