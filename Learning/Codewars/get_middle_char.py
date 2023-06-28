def get_middle(s):
    # when divided by 2, if there is a remainder, it is ODD. So when it's and ODD number...
    if len(s) % 2 != 0:
        # divide by 2 and add 0.5 (for rounding up)
        x = len(s) / 2 + 0.5
        x = round(x)
        # use index -1, because it needs to be the MIDDLE number
        mid = s[x-1]
    else:
        x = int(len(s) / 2)
        # need to add the x+1 add in range it does not include stop number
        mid = s[x-1:x+1]
    print(mid)


get_middle('HRTwJDDok')