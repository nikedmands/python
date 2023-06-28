# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'.
# Return the resulting string.
# 01011110001100111
# 45385593107843568


def fake_bin(x):
    result = ""
    for num in x:
        if int(num) < 5:
            result = result + "0"
        else:
            result = result + "1"
    print(result)
    return result


pass

fake_bin('45385593107843568')
