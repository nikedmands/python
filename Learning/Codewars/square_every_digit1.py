def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    print(int(ret))

square_digits(9119)