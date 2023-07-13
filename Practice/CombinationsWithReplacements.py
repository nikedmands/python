from itertools import combinations_with_replacement

s, n = 'RANK 3'.split()
n = int(n)
s = sorted(s)
for i in combinations_with_replacement(s, n):
    print("".join(i))



# in this example, combine each letter of RANK, 3 times with the other letters. Run to see result