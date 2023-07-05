def freq(sent):
    # crate a variable containing punctuation
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    # new string variable containing just alpha, currently empty
    no_punc = ""
    # for loop, to iterate over the original sentence and move alpha characters to new string variable
    for x in sent:
        if x not in punc:
            no_punc = no_punc + x
    # split new string variable to a list
    words = no_punc.split(' ')
    # counter is a dictionary, with key the word, and the value the count of that word in the list
    counter = {i: words.count(i) for i in words}
    # for loop, to iterate over the dictionary key, value pairs and just printing them
    for k, v in counter.items():
        print(k, "appears", v, "time(s)")


freq('Hello, my name!!!! name name:@ is Hello#][ Nik')

