from itertools import combinations_with_replacement

s, n = 'RANK 3'.split()
n = int(n)
s = sorted(s)
for j in combinations_with_replacement(s, n):
    print("".join(j))


# for i in range(len(lst)):
#     for j in range(len(lst)):
#         for k in range(len(lst)):
#             if i <= j and i <= k:
#                 answer.append(lst[i] + lst[j] + lst[k])
#             print(answer)




# ans = tuple(answer)
# for a in ans:
#     print(a)





#
#
# from itertool import combinations
# s, k = input().split()
# k = int(k)
# for i in range(1, k+1):
#     for comb in combinations(sorted(s), i):
#         SOUT = (''.join(comb))
#         print(SOUT)