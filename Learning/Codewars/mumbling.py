def accum(s):
    lst = []
    lst1 = []
    for i in s:
        lst.append(i)
    a = 0
    for i in lst:
        word = ""
        a += 1
        word = word + (str(a*i)).capitalize()
        lst1.append(word)
    answer = ""
    for i in lst1:
        answer = answer + '-' + i
    answer = answer.lstrip('-')
    print(answer)


accum('EvidjUnokmM')
