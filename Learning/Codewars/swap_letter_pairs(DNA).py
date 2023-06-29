def DNA_strand(dna):
    letters = []
    for i in dna:
        if i == 'A':
            letters.append('T')
        elif i == 'T':
            letters.append('A')
        elif i == 'G':
            letters.append('C')
        elif i == 'C':
            letters.append('G')
    word = ""
    for i in letters:
        word = word + i

    print(word)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ BEST ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))




DNA_strand('ATTGC')