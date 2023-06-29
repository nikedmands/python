def dominator(arr):
    if len(arr) == False:
        return -1
    else:
        length = len(arr)
        answer = {i: arr.count(i) for i in arr}
        max_count = max(answer.values())
        key = [k for k, v in answer.items() if float(v) == max_count]
        if max_count <= (length/2):
            return -1
        elif len(key) > 1 or False:
            return -1
        else:
            return key[0]

