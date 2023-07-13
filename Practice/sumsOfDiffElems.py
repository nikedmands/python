def max_sum(a):
    sums = []
    for i in range(len(a)):
        for j in range(len(a)):
            if i != j:
                sums.append(a[i] + a[j])
    print(sums)





max_sum([51, 71, 17, 42])