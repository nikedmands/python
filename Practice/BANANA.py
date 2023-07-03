def solutions(s):
    countB = 0
    countA = 0
    countN = 0
    for i in s:
        if i == 'B':
            countB += 1
        elif i == 'A':
            countA += 1
        elif i == 'N':
            countN += 1
    # print(countB)
    # print(countA)
    # print(countN)
    counter = 0
    while True:
        if countB >= 1 and countA >= 3 and countN >= 2:
            counter += 1
            countB -= 1
            countA -= 3
            countN -= 2
        else:
            break
    # print(countB)
    # print(countA)
    # print(countN)
    print(counter)



solutions("QABAAAWOBL")

# NAANAAXNABABYNNBZ
# B-A-N-A-N-A
# 1 B
# 3 A
# 2 N
# check = all(item in list1 for item in list2)